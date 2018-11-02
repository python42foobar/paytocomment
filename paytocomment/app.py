from flask import Flask
app = Flask(__name__)
app.config.from_object('paytocomment.config.ProductionConfig')


@app.route('/')
def hello_world():
    print(app.config)
    return 'Hello, World!'
