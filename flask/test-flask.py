from flask import Flask
from flask import render_template
print(__file__)
#创建flask实例
app = Flask(__name__)

#创建路由
@app.route('/test-for-life/templates/<name>')
def index(name):
    return render_template('hello.html',name = name)

if __name__ == '__main__':
    app.run()