import time
from functools import wraps


def mytimer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            start = time.time()
            result = f(*args, **kwargs)
            end = time.time()
            print("Time =  {} seconds".format(end - start))
            return result
        except:
            print('Something went wrong')
    return wrapper

def mylogger(f):
    import logging
    logging.basicConfig(filename='{}.log'.format(f.__name__), level=logging.INFO)
    @wraps(f)
    def wrapper(*args,**kwargs):
        try:            
            logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
            with open("mylogged.txt","w") as file:
                file.write(str(f(*args, **kwargs)))
            print("Logged successfully")
        except:
            print("Something went wrong")
    return wrapper


@mylogger
@mytimer
def f(a, b):
    return a+b

f(3, 3)