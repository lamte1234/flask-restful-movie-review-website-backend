from functools import wraps
from flask import request
from models.user import User

def test_decorator():
    def _test_decorator(f):
        @wraps(f)
        def __test_decorator(*args, **kwargs):
            print('testing')
            return f(*args, **kwargs)
        return __test_decorator
    return _test_decorator

def login_mdw():
    def _login_mdw(f):
        @wraps(f)
        def __login_mdw(*args, **kwargs):
            username = request.form['username']
            password = request.form['password']
            ### do some stuff here, hashing pass, checking regex to avoid sql injection, but now i want just to
            # focus on querying data from database.
            result = User.query.filter_by(username=username).first()
            if not result:
                return {'message': 'incorrect'}, 401
            else:
                if password != result.password:
                    return {'message': 'incorrect'}, 401
            
            return f(*args, **kwargs)
        return __login_mdw
    return _login_mdw