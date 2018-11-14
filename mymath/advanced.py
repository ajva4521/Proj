def add (a , b , c , d):
    if c is not None and d is not None:
        result = a + b + c + d
    elif c is not None:
        result = a + b + c
    else:
        result = a + b
    return result

##input? při odečítání on největšího po nejmenší?

def sub (a,b,c,d):
    if c is not None and d is not None:
        result = a - b - c - d
    elif c is not None:
        result = a - b - c
    else:
        result = a - b
    return result

def mul (a,b,c,d):
    if c is not None and d is not None:
        result = a * b * c * d
    elif c is not None:
        result = a * b * c
    else:
        result = a * b
    return result

#input? možnosti?

def div (a,b,c,d):
    if not b or not c or not d:
        result = "nulou nelze dělit"
    elif c is not None and d is not None:
        result = a / b / c / d
    elif c is not None:
        result = a / b / c
    else:
        result = a / b
    return result

def pow (a,b,c,d):
    if c is not None and d is not None:
        result = a ** b ** c ** d
    elif c is not None:
        result = a ** b ** c
    else:
        result = a ** b
    return result
# příliš velké číslo .. podmínka v podmínce?

def modulo (a,b):
    if b == 0:
        result = "nulou nelze dělit"
    else:
        result = a % b
    return result
