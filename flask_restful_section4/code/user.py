class User:
    def __init__(self, _id, username, password):
        '''
        We are using _id instead of id as id is a python key word
        '''
        self.id = _id
        self.username = username
        self.password = password
    