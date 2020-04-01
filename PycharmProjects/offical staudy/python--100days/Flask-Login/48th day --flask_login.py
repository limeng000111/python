from flask_login import LoginManager
from flask import Flask

from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo
from flask_wtf import FlaskForm
from flask import render_template,redirect,url_for,request
from flask_login import login_user
from werkzeug.security import generate_password_hash
import uuid


app = Flask(__name__) #创建Flask应用

app.secret_key = 'tester' #设置表单交互秘钥

login_manager = LoginManager() #实例化登录管理对象
login_manager.init_app(app)  #初始化应用
login_manager.login_view = 'login' #设置用户登录视图函数 endpoint

class LoginForm(FlaskForm):
    def __init__(self):

        '''登录表单类'''
        username = StringField('用户名',validators=[DataRequired()])
        password = StringField('密码',validators=[DataRequired()])
        Users = [
            {
                'id': 1,
                'name': 'lily',
                'passwd': generate_password_hash('123456')
            },
            {
                'id': 2,
                'name': 'jack',
                'passwd': generate_password_hash('123456')
            }
        ]
        self.Users = Users



    def creat_user(self,username,passwd):
        #创建一个用户
        user = {
            'name' : username,
            'passwd' : generate_password_hash(passwd),
            'uuid' : uuid.uuid4()
        }
        self.Users.append(user)

    def get_user(user_name):
        #根据用户名获取用户记录
        for user in self.Users:
            if user.get('name') == user_name:
                return user
        return None

    @app.route('/login/',methods=('GET','POST'))#登录的方式
    def login():
        form = LoginForm()
        emsg = None
        if form.validate_on_submit():
            user_name = form.username.data
            password = form.password.data
            user_info = get_user(user_name)
