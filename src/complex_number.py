import math


class ComplexNumber:

    def __init__(self, x: int|float, y: int|float):
        if not isinstance(x, (int, float)):
            raise TypeError(f"x must be int or float, not {type(x).__name__}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"y must be int or float, not {type(y).__name__}")
        self.x = x
        self.y = y
        self.mod = math.sqrt(x**2 + y**2)
        self.argument = (math.atan2(y, x)) % (2*math.pi)
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'ComplexNumber' and '{type(other).__name__}'")

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"unsupported operand type(s) for +: '{type(other).__name__}' and 'ComplexNumber'")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f"unsupported operand type(s) for -: 'ComplexNumber' and '{type(other).__name__}'")

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(other.x - self.x, other.y - self.y)
        else:
            raise TypeError(f"unsupported operand type(s) for -: '{type(other).__name__}' and 'ComplexNumber'")
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.x*other.x - self.y*other.y, self.x*other.y + self.y*other.x)
        else:
            raise TypeError(f"unsupported operand type(s) for *: 'ComplexNumber' and '{type(other).__name__}'")

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.x*other.x - self.y*other.y, self.x*other.y + self.y*other.x)
        else:
            raise TypeError(f"unsupported operand type(s) for *: '{type(other).__name__}' and 'ComplexNumber'")
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                (self.x*other.x + self.y*other.y) / (other.x**2 + other.y**2),
                (self.y*other.x - self.x*other.y) / (other.x**2 + other.y**2)
            )
        else:
            raise TypeError(f"unsupported operand type(s) for /: 'ComplexNumber' and '{type(other).__name__}'")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                (self.x*other.x + self.y*other.y) / (self.x**2 + self.y**2),
                (other.y*self.x - other.x*self.y) / (self.x**2 + self.y**2)
            )
        else:
            raise TypeError(f"unsupported operand type(s) for /: '{type(other).__name__}' and 'ComplexNumber'")
        
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            mod = self.mod**other
            argument = (other*self.argument) % (2*math.pi)
            return ComplexNumber(mod*math.cos(argument), mod*math.sin(argument))
        elif isinstance(other, ComplexNumber):
            result = ComplexNumber.exp((math.log(self.mod)+ComplexNumber(0, 1)*self.argument)*other)
            return result
        else:
            raise TypeError(f"unsupported operand type(s) for **: 'ComplexNumber' and '{type(other).__name__}'")

    def __rpow__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if isinstance(other, ComplexNumber):
            result = ComplexNumber.exp((math.log(other.mod)+ComplexNumber(0, 1)*other.argument)*self)
            return result
        else:
            raise TypeError(f"unsupported operand type(s) for **: '{type(other).__name__}' and 'ComplexNumber'")

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return self.x==other.x and self.y==other.y
    
    def __ne__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return self.x!=other.x or self.y!=other.y

    @staticmethod
    def exp(complex):
        """
        This expression is multivalued, so we consider the angle congruent to 360 degrees.
        """
        if isinstance(complex, (int, float)):
            complex = ComplexNumber(complex, 0)
        if isinstance(complex, ComplexNumber):
            mod = math.e**complex.x
            argument = (complex.y) % (2*math.pi)
            return ComplexNumber(mod*math.cos(argument), mod*math.sin(argument))
        else:
            raise TypeError(f"exp() expected a ComplexNumber, int, or float instance, not '{type(complex).__name__}'. ")

    @staticmethod
    def ln(complex):
        """
        This expression is multivalued, so we consider the angle congruent to 360 degrees.
        """
        if isinstance(complex, (int, float)):
            complex = ComplexNumber(complex, 0)
        if isinstance(complex, ComplexNumber):
            return ComplexNumber(math.log(complex.mod), complex.argument)
        else:
            raise TypeError(f"ln() expected a ComplexNumber, int, or float instance, not '{type(complex).__name__}'. ")

    @staticmethod
    def log(complex, base=math.e):
        """
        This expression is multivalued, so we consider the angle congruent to 360 degrees.
        """
        if isinstance(complex, (int, float)):
            complex = ComplexNumber(complex, 0)
        if isinstance(complex, ComplexNumber):
            result = ComplexNumber.ln(complex) / ComplexNumber.ln(base)
            return ComplexNumber(result.x, result.y)
        else:
            raise TypeError(f"log() expected a ComplexNumber, int, or float instance, not '{type(complex).__name__}'. ")
    
    def __pos__(self):
        return ComplexNumber(self.x, self.y)
    
    def __neg__(self):
        return ComplexNumber(-self.x, -self.y)
    
    def __bool__(self):
        if self.x == self.y == 0:
            return False
        return True

    def __str__(self):
        return f"{self.x} + {self.y}i"
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index == 0:
            return self.x
        elif index == 1 or index == -1:
            return self.y
        else:
            raise IndexError("Index out of range")
    
    def __len__(self):
        return 2