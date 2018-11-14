def factorial(a):
    if a < 0:
        raise Exception("negative number")
    r = 1
    while a > 1:
        r = r * a
        a = a - 1
    return r
