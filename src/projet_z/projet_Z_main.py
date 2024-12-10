# src/projet_Z/projet_Z_main.py

def addition(a,b):
    """
    Additionne deux nombres.
    
    :param a: Premier nombre
    :param b: Deuxième nombre
    :return: La somme de a et b
    """
    return a+b

def soustraction(a,b):
    """
    Soustrait deux nombres.
    
    :param a: Premier nombre
    :param b: Deuxième nombre
    :return: La différence entre a et b
    """
    return a-b

def multiplication(a,b):
    """
    Multiplie deux nombres.
    
    :param a: Premier nombre
    :param b: Deuxième nombre
    :return: Le produit de a et b
    """
    return a*b

def division(a,b):
    """
    Divise deux nombres.
    
    :param a: Premier nombre
    :param b: Deuxième nombre
    :return: Le quotient de a divisé par b
    :raises ZeroDivisionError: Si b est zéro
    """
    if b==0:
        raise ZeroDivisionError("La division par zéro n'est pas permise.")
    return a/b

def division_euclidienne(a,b):
    """
    Effectue une division euclidienne entre deux nombres.
    
    :param a: Premier nombre
    :param b: Deuxième nombre
    :return: Le quotient entier de a divisé par b
    :raises ZeroDivisionError: Si b est zéro
    """
    if b==0:
        raise ZeroDivisionError("La division euclidienne par zéro n'est pas permise.")
    return a//b
