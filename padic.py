"""
P-adic number implementation.

This module provides the PAdic class for representing and manipulating p-adic numbers.
Based on the design specification in P_ADIC_DESIGN.md.
"""

from fractions import Fraction
from typing import Union, Optional


class PAdic:
    """
    P-adic number representation.
    
    A p-adic number is represented as a series: a_k * p^k + a_{k+1} * p^{k+1} + ...
    where k is the valuation and each a_i is a digit 0 ≤ a_i < p.
    """
    
    def __init__(self, value: Union[int, Fraction, 'PAdic'], prime: int, precision: int = 20):
        """
        Construct a p-adic number.
        
        Args:
            value: The number to represent as a p-adic. Can be:
                - int: Integer value
                - Fraction: Rational number (from fractions module)
                - PAdic: Another p-adic number (copy constructor)
            
            prime: Prime number p for the p-adic representation (must be prime)
            
            precision: Number of p-adic digits to maintain (default: 20)
        
        Raises:
            ValueError: If prime is not prime, or value cannot be converted
            ZeroDivisionError: If attempting to represent a rational with denominator 0
        """
        self.prime = prime
        self.precision = precision
        self.valuation = 0
        self.digits = []
        self.is_zero = False
        
        # TODO: Implement validation and conversion logic for rational to p-adic
        # This stub will store input but won't perform actual p-adic conversion
        if value == 0:
            self.is_zero = True
        else:
            # Stub implementation - doesn't perform actual p-adic conversion yet
            self.is_zero = False
            # The actual implementation would:
            # 1. Factor out powers of p from numerator and denominator  
            # 2. Use long division in base p for the remaining fraction
            # 3. Handle repeating patterns for infinite expansions
            raise NotImplementedError(f"P-adic conversion not yet implemented for value {value} - this is a stub for TDD")
    
    def to_rational(self, max_denominator_power: Optional[int] = None) -> Fraction:
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
        """
        # Handle zero case (this should work)
        if self.is_zero:
            return Fraction(0)
        
        # TODO: Implement actual p-adic to rational conversion using Horner's method
        # This is a stub implementation that will fail tests to demonstrate TDD
        raise NotImplementedError("to_rational method not yet implemented for non-zero values - this is a stub for TDD")
    
    def to_int(self) -> int:
        """
        Convert to integer if possible (valuation >= 0 and finite representation).
        
        Returns:
            int: Integer value
            
        Raises:
            ValueError: If number is not an integer
        """
        # TODO: Implement actual conversion logic
        rational = self.to_rational()
        if rational.denominator == 1:
            return rational.numerator
        else:
            raise ValueError(f"P-adic number {self} is not an integer")
    
    def to_series_string(self, show_digits: int = 10) -> str:
        """
        Convert to human-readable series representation.
        
        Args:
            show_digits: Number of terms to display
            
        Returns:
            str: String like "2 + 1*5 + 3*5^2 + O(5^3)"
        """
        # TODO: Implement actual series representation
        return f"PAdic({self._original_value if hasattr(self, '_original_value') else 0}, {self.prime})"
    
    @classmethod  
    def from_int(cls, integer: int, prime: int, precision: int = 20) -> 'PAdic':
        """
        Create p-adic number from integer.
        
        Args:
            integer: Integer value
            prime: Prime for p-adic representation  
            precision: Number of digits to maintain
            
        Returns:
            PAdic: P-adic representation of the integer
        """
        return cls(integer, prime, precision)
    
    def __eq__(self, other: 'PAdic') -> bool:
        """Check equality with another PAdic number."""
        # TODO: Implement proper equality check
        if not isinstance(other, PAdic):
            return False
        return (self.prime == other.prime and 
                self.to_rational() == other.to_rational())
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"PAdic({self._original_value if hasattr(self, '_original_value') else 0}, {self.prime}, precision={self.precision})"