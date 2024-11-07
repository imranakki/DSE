def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Can't divide by zero"