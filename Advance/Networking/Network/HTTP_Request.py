# HTTP : Hyper Text Transfer Protocol
# requests module : handle request and response, authentication, compression/decompression, chunked requests.

# HTTP client sends an HTTP request to a server in the form of a request message which includes:
# Request-Line
# Zero or more Header(General|Request|Entity)
# Empty-Line : End of Header
# Message body(Optional)

# Request-Line:
# Request-Line = Method SP Request-URI SP HTTP-Version CRLF

# Request Method:
# GET: To retrieve information from the given server using a given URI.
# requests.get(url, params=None, **kwargs)
# url : URL for the new :class:`Request` object.
# params : (optional) Dictionary, list of tuples or bytes to send in the query string for the :class:`Request`.
# rtype: requests.Response

# get(
#     url: Text | bytes,
#     params: _Params | None = ...,
#     data: Any | None = ...,
#     headers: Any | None = ...,
#     cookies: Any | None = ...,
#     files: Any | None = ...,
#     auth: Any | None = ...,
#     timeout: Any | None = ...,
#     allow_redirects: bool = ...,
#     proxies: Any | None = ...,
#     hooks: Any | None = ...,
#     stream: Any | None = ...,
#     verify: Any | None = ...,
#     cert: Any | None = ...,
#     json: Any | None = ...,
# ) -> Response: ...

import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth
from requests.auth import AuthBase
from requests.exceptions import Timeout
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from urllib3 import HTTPConnectionPool

response = requests.get('https://api.github.com')
print(response)
print(response.status_code)
print(response.reason)
# response.content gives row bytes of response payload.
# print(response.content)
# response.text gives UTF-8 encoded string.
response.encoding = 'UTF-8'  # Optional: requests infers this internally
print(response.text)

# Headers:
print(response.headers)
print(response.headers['Content-Type'])
# print(response.headers['content-type'])


# Query String Parameters:
# To customize GET request, pass valve through query string parameters.
r = requests.get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'}, )

# As Tuple List:
# r = requests.get('https://api.github.com/search/repositories', params=[('q', 'requests+language:python')], )
# As Bytes:
# r = requests.get('https://api.github.com/search/repositories', params=b'q=requests+language:python', )

jsonResponse = r.json()
repository = jsonResponse['items'][0]
print("Repository name :", repository['name'], ", Description :", repository['description'])

# Request Headers:
# To customize headers, pass dictionary of HTTP headers using headers parameter.
response = requests.get('https://api.github.com/search/repositories',
                        params={'q': 'requests+language:python'},
                        headers={'Accept': 'application/vnd.github.v3.text-match+json'},
                        )

# View the new `text-matches` array which provides information about your search term within the results.
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

# Other HTTP methods:
# response = requests.head('https://httpbin.org/get')
# print(response.headers['Content-Type'])

# response = requests.delete('https://httpbin.org/delete')
# json_response = response.json()
# print(json_response['args'])


# Message Body:
# POST, PUT, and PATCH requests pass their data through the message body rather than parameters in the query string.
# pass payload to the corresponding function’s data parameter.

response = requests.post('https://httpbin.org/post', json={'key': 'value'})
# requests.post('https://httpbin.org/post', data=[('key', 'value')])
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])

# Inspecting Request:
print(response.request.headers['Content-Type'])
print(response.request.url)
print(response.request.body)


# Authentication:
# requests provides methods of authentication such as HTTPBasicAuth, HTTPDigestAuth and HTTPProxyAuth.

# user_URL = 'https://api.github.com/user'
# r = requests.get(user_URL, auth=('username', getpass()))  # Apply credentials using HTTPBasicAuth
# print(r.status_code)
#
# r = requests.get(user_URL)
# print(r.status_code)
#
# r = requests.get(user_URL, auth=HTTPBasicAuth('username', getpass()))
# print(r.status_code)


# Manual Authentication mechanism:
class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r


response = requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))
print(response)

# SSL certificate verification:
# True by default.
# The way that you communicate with secure sites over HTTP is by establishing an encrypted connection using SSL,
# which means that verifying the target server’s SSL Certificate is critical.
# False : disable SSL certification verification.
response = requests.get('https://api.github.com', verify=False)
print("SSL certificate verification :", response)

# Timeout:
# When an inline request is made to an external service, system will need to wait upon the response before moving on.
response = requests.get('https://api.github.com', timeout=3.05)
print(response)

# pass Tuple:
# First element : connect timeout(Time it allows for the client to establish a connection to the server)
# second element : read timeout(time it will wait on a response once your client has established a connection)
response = requests.get('https://api.github.com', timeout=(2, 5))
print(response)

# If the request times out, then the function will raise a Timeout exception:
try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')

# Max Retries:
# When a request fails, you may want your application to retry the same request.
# requests will not do this for you by default.
# Need to implement a custom Transport Adapter.

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    r = session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
else:
    print(r)


# Connection re-use
pool = HTTPConnectionPool('ajax.googleapis.com', maxsize=1)
r = pool.request('GET', '/ajax/services/search/web',
                 fields={'q': 'python', 'v': '3.0'})
print('Response Status:', r.status)
print('Header: ', r.headers['content-type'])
print('Python: ', len(r.data))


r = pool.request('GET', '/ajax/services/search/web',
                 fields={'q': 'php', 'v': '1.0'})
print('php: ', len(r.data))
print('Number of Connections: ', pool.num_connections)
print('Number of requests: ', pool.num_requests)
