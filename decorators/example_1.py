from functools import wraps


def decorator_maker_with_arguments(*args, **kwargs):
    '''
    This is an example of a Decorator that takes arguments.

    '''
    print(args, kwargs)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''
                Do Work
            '''
            print(args, kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def decorator(func):
    '''
    This is an example of a Decorator that does not take arguments.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        '''
            Do Work
        '''
        print("wrapper")
        return func(*args, **kwargs)

    return wrapper


@decorator
def inner_func():
    print("Inner Func")


@decorator_maker_with_arguments(test="test")
def inner_func_with_args(msg):
    print(msg)


def main():
    # inner_func()
    inner_func_with_args("Inner Func")


if __name__ == "__main__":
    main()
