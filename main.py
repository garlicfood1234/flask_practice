from flask import Flask

app = Flask(__name__)

@app.route('/')
def index() : 
    return "Hello, World!"


@app.route('/test/<int:num>')
def test(num) : 
    return str(num)

if __name__ == '__main__' : 
    app.run(host = '0.0.0.0', port = 80)
