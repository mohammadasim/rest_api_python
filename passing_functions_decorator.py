'''
Decorators is an advance python topic. Decorators allow you to decotate a function. Suppose we have a function and we want to add 
extra functionality to it.  There are two options first is to add extra code to the existing function, the problem is that as we have
modified the old function its functionality has changed and hence we can't call is easily.
Another option is to create a new function copy the code from the previous function and then add new code to it, but it means 
we had to rewrite the code, even though it is simple copy and paste.
But what if we then want to remove that extra functionality. We would need to delete it manually or make sure to have the old function
A better way is to have an on/off switch to quickly add this functionality.
Python has decorators that allow us to tack on extra functionality to an already existing function.
We use the @ operator and are then placed on top of the original function.
A decorator is just a function that gets called before the other function.
'''


# We import functools
import functools

def my_decorator(hello):
    @functools.wraps(hello)
    def fuction_that_runs_hello():
        print("In the decorator")
        hello()
        print("After running the docorator")
    return fuction_that_runs_hello

@my_decorator
def decorated_function():
    print("Hello world!")

decorated_function()