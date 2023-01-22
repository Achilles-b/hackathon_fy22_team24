### 参考URL：https://aiacademy.jp/media/?p=57

from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hello/<name>')
def hello(name):
    print(name) # <- localhost:8000/hello/<name> 部分
    return name

app.run(port=8000, debug=True)
