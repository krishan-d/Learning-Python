# Status code:
# 1xx: Informational
# It means the request was received and the process is continuing.
# 2xx: Success
# It means the action was successfully received, understood, and accepted.
# 3xx: Redirection
# It means further action must be taken in order to complete the request.
# 4xx: Client Error
# It means the request contains incorrect syntax or cannot be fulfilled.
# 5xx: Server Error
# It means the server failed to fulfill an apparently valid request.


import urllib3


http = urllib3.PoolManager()

resp = http.request('GET', 'http://tutorialspoint.com/robots.txt')
print(resp.data)

# get the status of the response
print(resp.status)
