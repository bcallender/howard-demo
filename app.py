from flask import Flask

app = Flask(__name__)

def greeting():
    return "Hey"

@app.route('/')
def hello_world():
    return '{} World!'.format(greeting())


if __name__ == '__main__':
    app.run()
