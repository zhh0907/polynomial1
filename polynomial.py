#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:30:48 2024

@author: skiter
"""

class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, x_value):
        return x_value

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, x_value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x_value):
        return self.p1.evaluate(x_value) + self.p2.evaluate(x_value)
    
class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, (Add, Div, Sub)):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, (Add, Div, Sub)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, x_value):
        return self.p1.evaluate(x_value) * self.p2.evaluate(x_value)
    
class Div:
    def __init__(self, p1, p2):
        if p2 == 0 or (isinstance(p2, Int) and p2.i == 0):
            raise Exception("Cannot divide by zero")
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, (Add, Mul, Sub)):
            if isinstance(self.p2, (Add, Mul)):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, (Add, Mul, Sub)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    
    def evaluate(self, x_value):
        divider = self.p2.evaluate(x_value)
        if divider == 0:
            raise Exception("Cannot divide by zero")
        return self.p1.evaluate(x_value) / divider
    
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Mul, Div)):
            if isinstance(self.p2, (Add, Mul, Div)):
                return "( " + repr(self.p1) + " ) - ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) - " + repr(self.p2)
        if isinstance(self.p2, (Add, Mul, Div)):
            return repr(self.p1) + " - ( " + repr(self.p2) + " )"
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, x_value):
        return self.p1.evaluate(x_value) - self.p2.evaluate(x_value)

        


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))
