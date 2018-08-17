items = []
item = list(filter(lambda x: x['name'] == name, items))
print(type(item))

from user import User
users = [
    User(1,'bob','asdf')
]

username_mapping = { u.username: u for u in users}
print(username_mapping)