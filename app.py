from flask import Flask
import settings as s
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello {}!'.format(s.NAME)


if __name__ == '__main__':
    app.run()
