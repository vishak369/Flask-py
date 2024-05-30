from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()