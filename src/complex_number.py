import math
import numbers
import operator


class ComplexNumber:

    __slots__ = ("_x", "_y")
    __array_ufunc__ = None

    def __init__(self, x: float, y: float):
        if not ComplexNumber._is_real(x):
            raise TypeError(f"x must be a real number, not {type(x).__name__}")
        if not ComplexNumber._is_real(y):
            raise TypeError(f"y must be a real number, not {type(y).__name__}")
        self._x = float(x)
        self._y = float(y)

    @staticmethod
    def _is_real(value) -> bool:
        if type(value) is float or type(value) is int:
            return True
        return isinstance(value, numbers.Real) and not isinstance(value, bool)

    @staticmethod
    def _coerce(value):
        if isinstance(value, ComplexNumber):
            return value
        if ComplexNumber._is_real(value):
            return ComplexNumber(value, 0.0)
        return None

    @staticmethod
    def _require(value, function_name: str):
        number = ComplexNumber._coerce(value)
        if number is None:
            raise TypeError(
                f"{function_name}() expected a ComplexNumber or a real number, not '{type(value).__name__}'"
            )
        return number

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def mod(self) -> float:
        return math.hypot(self._x, self._y)

    @property
    def argument(self) -> float:
        angle = math.atan2(self._y, self._x)
        return math.pi if angle == -math.pi else angle

    def __add__(self, other):
        other = ComplexNumber._coerce(other)
        if other is None:
            return NotImplemented
        return ComplexNumber(self._x + other._x, self._y + other._y)

    __radd__ = __add__

    def __sub__(self, other):
        other = ComplexNumber._coerce(other)
        if other is None:
            return NotImplemented
        return ComplexNumber(self._x - other._x, self._y - other._y)

    def __rsub__(self, other):
        other = ComplexNumber._coerce(other)
        if other is None:
            return NotImplemented
        return other - self

    def __mul__(self, other):
        other = ComplexNumber._coerce(other)
        if other is None:
            return NotImplemented
        return ComplexNumber(
            self._x*other._x - self._y*other._y,
            self._x*other._y + self._y*other._x,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = ComplexNumber._coerce(other)
        if other is None:
            return NotImplemented
        denominator = other._x**2 + other._y**2
        if denominator == 0:
            raise ZeroDivisionError("complex division by zero")
        return ComplexNumber(
            (self._x*other._x + self._y*other._y) / denominator,
            (self._y*other._x - self._x*other._y) / denominator,
        )

    def __rtruediv__(self, other):
        other = ComplexNumber._coerce(other)
        if other is None:
            return NotImplemented
        return other / self

    def __pow__(self, other):
        exponent = ComplexNumber._coerce(other)
        if exponent is None:
            return NotImplemented
        if exponent._y == 0 and exponent._x.is_integer():
            return self._int_pow(int(exponent._x))
        if not self:
            if exponent._x > 0:
                return ComplexNumber(0.0, 0.0)
            raise ZeroDivisionError("0 cannot be raised to a power with non-positive real part")
        return ComplexNumber.exp(exponent * ComplexNumber.ln(self))

    def __rpow__(self, other):
        base = ComplexNumber._coerce(other)
        if base is None:
            return NotImplemented
        return base ** self

    def _int_pow(self, n: int):
        if n < 0:
            return (1 / self)._int_pow(-n)
        result = None
        base = self
        while n:
            if n & 1:
                result = base if result is None else result * base
            n >>= 1
            if n:
                base = base * base
        if result is None:
            return ComplexNumber(1.0, 0.0)
        if not (math.isfinite(result._x) and math.isfinite(result._y)) \
                and math.isfinite(self._x) and math.isfinite(self._y):
            raise OverflowError("complex exponentiation")
        return result

    def __eq__(self, other):
        other = ComplexNumber._coerce(other)
        if other is None:
            return NotImplemented
        return self._x == other._x and self._y == other._y

    def __hash__(self):
        if self._y == 0:
            return hash(self._x)
        return hash((self._x, self._y))

    @staticmethod
    def exp(z):
        z = ComplexNumber._require(z, "exp")
        magnitude = math.exp(z._x)
        return ComplexNumber(magnitude*math.cos(z._y), magnitude*math.sin(z._y))

    @staticmethod
    def ln(z):
        z = ComplexNumber._require(z, "ln")
        if not z:
            raise ValueError("ln(0) is undefined")
        return ComplexNumber(math.log(z.mod), z.argument)

    @staticmethod
    def log(z, base=math.e):
        z = ComplexNumber._require(z, "log")
        base = ComplexNumber._require(base, "log")
        return ComplexNumber.ln(z) / ComplexNumber.ln(base)

    def __pos__(self):
        return self

    def __neg__(self):
        return ComplexNumber(-self._x, -self._y)

    def __abs__(self):
        return self.mod

    def __bool__(self):
        return self._x != 0 or self._y != 0

    def __repr__(self):
        return f"ComplexNumber({self._x!r}, {self._y!r})"

    def __str__(self):
        sign = "-" if self._y < 0 else "+"
        return f"{self._x} {sign} {abs(self._y)}i"

    def __getitem__(self, index):
        index = operator.index(index)
        if index in (0, -2):
            return self._x
        if index in (1, -1):
            return self._y
        raise IndexError("ComplexNumber index out of range")

    def __len__(self):
        return 2