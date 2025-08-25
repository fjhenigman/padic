# P-adic Number Implementation Design

This document specifies the design for p-adic number representation and conversion routines in Python.

## Overview

P-adic numbers extend the rational numbers by completing them with respect to the p-adic metric, where a prime p determines the notion of "smallness" based on divisibility. Every non-zero p-adic number can be uniquely represented as an infinite series:

```
x = a_k * p^k + a_{k+1} * p^{k+1} + a_{k+2} * p^{k+2} + ...
```

where k is the p-adic valuation of x, and 0 ≤ a_i < p for all i ≥ k, with a_k ≠ 0.

## P-adic Number Constructor

### Class Definition

```python
class PAdic:
    def __init__(self, value, prime, precision=20):
        """
        Construct a p-adic number.
        
        Args:
            value: The number to represent as a p-adic. Can be:
                - int: Integer value
                - Fraction: Rational number (from fractions module)
                - tuple: (rational_num, rational_den) representing rational_num/rational_den
                - list: List of p-adic digits [a_k, a_{k+1}, ..., a_{k+n}] with optional valuation
                - str: String representation like "3*5^2 + 2*5^3 + 1*5^4" or "1/5 + 2 + 3*5"
                - PAdic: Another p-adic number (copy constructor)
            
            prime: Prime number p for the p-adic representation (must be prime)
            
            precision: Number of p-adic digits to maintain (default: 20)
        
        Raises:
            ValueError: If prime is not prime, or value cannot be converted
            ZeroDivisionError: If attempting to represent a rational with denominator 0
        """
```

### Constructor Examples

```python
# From integers
x = PAdic(42, 5)  # 42 in 5-adic representation

# From rational numbers
from fractions import Fraction
y = PAdic(Fraction(3, 7), 5)  # 3/7 in 5-adic representation
z = PAdic((3, 7), 5)  # Same as above using tuple

# From p-adic digit sequence (starting from p^valuation)
w = PAdic([2, 1, 3], 5, valuation=-1)  # 2*5^(-1) + 1*5^0 + 3*5^1

# From string representation
s = PAdic("1/5 + 2 + 3*5", 5)  # 1*5^(-1) + 2*5^0 + 3*5^1

# Copy constructor
u = PAdic(x, 5)  # Copy of x
```

### Internal Representation

```python
class PAdic:
    def __init__(self, value, prime, precision=20):
        self.prime = prime          # The prime p
        self.precision = precision  # Number of digits to maintain
        self.valuation = 0         # Lowest power of p (can be negative)
        self.digits = []           # List of p-adic digits [a_k, a_{k+1}, ...]
        self.is_zero = False       # Special flag for zero
        
        # Validation and conversion logic here
```

## Conversion Routines

### 1. P-adic to Rational Conversion

```python
def to_rational(self, max_denominator_power=None):
    """
    Convert p-adic number to a rational approximation.
    
    For p-adic numbers with non-negative valuation, this gives an exact
    rational representation. For negative valuations, this may give an
    approximation based on the finite precision.
    
    Args:
        max_denominator_power: Maximum power of p allowed in denominator.
                             If None, uses the absolute value of the minimum valuation.
    
    Returns:
        Fraction: Rational approximation of the p-adic number
        
    Raises:
        ValueError: If the p-adic number cannot be represented as a rational
                   within the given constraints
    
    Examples:
        >>> x = PAdic([2, 1, 3], 5, valuation=0)  # 2 + 1*5 + 3*5^2 = 77
        >>> x.to_rational()
        Fraction(77, 1)
        
        >>> y = PAdic([1], 5, valuation=-1)  # 1*5^(-1) = 1/5
        >>> y.to_rational()
        Fraction(1, 5)
    """
```

### 2. Rational to P-adic Conversion

```python
@classmethod
def from_rational(cls, rational, prime, precision=20):
    """
    Convert a rational number to p-adic representation.
    
    This implements the standard algorithm for p-adic expansion of rationals:
    1. Factor out powers of p from numerator and denominator
    2. Use long division in base p for the remaining fraction
    3. Handle repeating patterns for infinite expansions
    
    Args:
        rational: Fraction object or tuple (num, den) representing num/den
        prime: Prime number for p-adic representation
        precision: Number of p-adic digits to compute
    
    Returns:
        PAdic: P-adic representation of the rational number
        
    Raises:
        ValueError: If the rational cannot be represented (e.g., if denominator
                   has prime factors other than p that don't cancel)
    
    Examples:
        >>> PAdic.from_rational(Fraction(7, 25), 5)  # 7/25 = 7/5^2
        PAdic with digits representing 7 * 5^(-2)
        
        >>> PAdic.from_rational(Fraction(1, 3), 5)  # 1/3 in 5-adics
        PAdic with repeating expansion
    """
```

### Alternative Conversion Methods

```python
def to_int(self):
    """
    Convert to integer if possible (valuation >= 0 and finite representation).
    
    Returns:
        int: Integer value
        
    Raises:
        ValueError: If number is not an integer
    """

def to_series_string(self, show_digits=10):
    """
    Convert to human-readable series representation.
    
    Args:
        show_digits: Number of terms to display
        
    Returns:
        str: String like "2 + 1*5 + 3*5^2 + O(5^3)"
    """

@classmethod  
def from_int(cls, integer, prime, precision=20):
    """
    Create p-adic number from integer.
    
    Args:
        integer: Integer value
        prime: Prime for p-adic representation  
        precision: Number of digits to maintain
        
    Returns:
        PAdic: P-adic representation of the integer
    """
```

## Usage Examples

### Basic Construction and Conversion

```python
from fractions import Fraction

# Create p-adic numbers
x = PAdic(42, 5)                    # Integer to 5-adic
y = PAdic(Fraction(3, 7), 5)        # Rational to 5-adic  
z = PAdic("2 + 3*5 + 1*5^2", 5)     # String to 5-adic

# Convert back to rationals
print(x.to_rational())              # Fraction(42, 1)
print(y.to_rational())              # Fraction(3, 7)
print(z.to_rational())              # Fraction(42, 1)  # 2 + 15 + 25 = 42

# Alternative constructors
a = PAdic.from_rational(Fraction(1, 6), 5)
b = PAdic.from_int(100, 7)
```

### Working with Precision

```python
# High precision for accurate computations
x = PAdic(Fraction(1, 3), 5, precision=50)

# Limited precision for efficiency
y = PAdic(Fraction(1, 3), 5, precision=10)

# Check if conversion is exact
rational_approx = x.to_rational()
exact = (x == PAdic.from_rational(rational_approx, 5))
```

### Handling Special Cases

```python
# Zero
zero = PAdic(0, 5)
assert zero.is_zero == True

# Negative numbers
neg = PAdic(-42, 5)

# Very large numbers
big = PAdic(5**100, 5)  # High valuation

# Very small numbers (negative valuation)
small = PAdic(Fraction(1, 5**10), 5)  # Valuation -10
```

## Implementation Notes

### Internal Algorithms

1. **Rational to P-adic**: Use extended Euclidean algorithm to extract p-adic valuation, then perform base-p long division.

2. **P-adic to Rational**: Horner's method to evaluate the polynomial representation.

3. **Precision Handling**: Maintain fixed precision and handle overflow/underflow appropriately.

4. **Validation**: Ensure prime is actually prime using primality test.

### Performance Considerations

- Store digits in little-endian order (lowest power first) for efficient arithmetic
- Use lazy evaluation for infinite expansions
- Implement caching for frequently used rational conversions
- Optimize for common cases (integers, simple fractions)

### Error Handling

- Validate prime numbers on construction
- Handle division by zero appropriately  
- Provide clear error messages for invalid inputs
- Support graceful degradation for precision limits

This design provides a robust foundation for p-adic arithmetic while maintaining ease of use and mathematical correctness.