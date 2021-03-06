from werkzeug.security import safe_str_cmp
from models.user import UserModel
'''
Since In the users list above we have instances of user class.
In the username_mapping we first select the username and then use list comprehension to give us
the variable and values or attributes of the user object. so the result is bob: {id:1, username:'bob',password:'asdf'} we 
have to remeber that when we create an object we assign to each attribute the value passed to it.
'''

def authenticate(username, password):
    '''
    we have used the get() method to get value of a key from a dictionary.
    The benefit is using this is that we can return None if there isn't any match for the key
    '''
    user = UserModel.find_by_username(username)
    #When comparing strings there can be issues with encodring etc. hence we user safe_str_cmp (safe string compare)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    '''
    This function is unique to Flask-Jwt.It takes the payload returned by this 
    library as a parameter and we have to extract the userid from it.
    '''
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

