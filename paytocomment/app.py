from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object('paytocomment.config.ProductionConfig')
app.secret_key = app.config.get('SECRET_KEY')


@app.route('/')
def hello_world():
    print(app.config.get('DATABASE_URI'))
    return render_template('index.html')
