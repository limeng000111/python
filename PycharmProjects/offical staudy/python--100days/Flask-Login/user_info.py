from werkzeug.security import generate_password_hash

Users = [
    {
        'id' : 1,
        'name' : 'lily',
        'passwd' : generate_password_hash('123456')
    },
    {
        'id' : 2,
        'name' : 'jack',
        'passwd' : generate_password_hash('123456')
    }
]
print(generate_password_hash('123456'))