from werkzeug.security import generate_password_hash
import uuid

USERS = []

def creat_user(username,passwd):
    #创建一个用户
    user = {
        'name' : username,
        'passwd' : generate_password_hash(passwd),
        'uuid' : uuid.uuid4()
    }
    USERS.append(user)

def get_user(user_name):
    #根据用户名获取用户记录
    for user in USERS:
        if user.get('name') == user_name:
            return user
    return None