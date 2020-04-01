#创建用户类  类维护登录状态
from flask_login import UserMixin #引入用户基类
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_login import login_manager
import


class User(UserMixin):
    '''用户类'''
    def __init__(self,user):
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
        self.username = user.get('name')
        self.password_hash = user.get('passwd')
        self.id = user.get('id')

    def verify_password(self,password):
        if self.password_hash is None:
            return None
        return check_password_hash(self.password_hash,password)

    def get_id(self):
        '''获取用户ID'''
        return self.id

    @staticmethod
    def get(self,user_id):
        if not user_id:
            return None
        for user in self.Users:
            if user.get('id') == user_id:
                return User(user)
        return None

    @login_manager.user_loader  #定义获取登录用户的方法
    def load_user(user_id):
        return User.get(user_id)