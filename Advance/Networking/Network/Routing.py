# http://127.0.0.1:5000/

# Routing:
# The mechanism of mapping the URL directly to the code that creates the webpage.
# For better management of the structure of the webpage and increases the performance of the site considerably and -
# further enhancements or modifications become really straight forward.

# Routing in Flask:
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hi Eve!'

if __name__ == '__main__':
    app.run()

