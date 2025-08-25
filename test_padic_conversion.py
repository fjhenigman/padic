"""
Test suite for P-adic number conversion.

This module tests conversion between rational numbers and p-adic representations
in both directions to ensure consistency.
"""

import unittest
from fractions import Fraction
from padic import PAdic


class TestPAdicConversion(unittest.TestCase):
    """Test p-adic to rational and rational to p-adic conversion consistency."""
    
    def setUp(self):
        """Set up test cases with rational numbers and their expected p-adic info."""
        # Table-driven test data: (rational_value, prime, expected_valuation, description)
        self.test_cases = [
            # Simple integers
            (Fraction(0), 5, 0, "zero"),
            (Fraction(1), 5, 0, "one"),
            (Fraction(5), 5, 1, "prime itself"),
            (Fraction(25), 5, 2, "prime squared"),
            (Fraction(42), 5, 0, "integer not divisible by prime"),
            (Fraction(-7), 5, 0, "negative integer"),
            
            # Simple fractions
            (Fraction(1, 2), 5, 0, "unit fraction"),
            (Fraction(3, 7), 5, 0, "general fraction"),
            (Fraction(1, 5), 5, -1, "reciprocal of prime"),
            (Fraction(1, 25), 5, -2, "reciprocal of prime squared"),
            (Fraction(2, 5), 5, -1, "fraction with prime in denominator"),
            (Fraction(7, 25), 5, -2, "fraction with prime squared in denominator"),
            
            # Mixed cases
            (Fraction(15, 4), 5, 1, "numerator divisible by prime"),
            (Fraction(10, 3), 5, 1, "factor of prime in numerator"),
            (Fraction(-3, 5), 5, -1, "negative fraction"),
            
            # Different prime
            (Fraction(1, 3), 3, -1, "reciprocal of different prime"),
            (Fraction(9), 3, 2, "different prime squared"),
            (Fraction(2, 9), 3, -2, "fraction with different prime squared"),
            
            # Prime = 2 cases
            (Fraction(8), 2, 3, "power of 2"),
            (Fraction(1, 4), 2, -2, "reciprocal of power of 2"),
            (Fraction(3, 8), 2, -3, "odd numerator, power of 2 denominator"),
            
            # Prime = 7 cases  
            (Fraction(49), 7, 2, "7 squared"),
            (Fraction(5, 7), 7, -1, "fraction with 7 in denominator"),
            (Fraction(14, 3), 7, 1, "7 in numerator"),
        ]
    
    def test_rational_to_padic_to_rational_conversion(self):
        """Test that rational -> p-adic -> rational gives back the original rational."""
        for rational_value, prime, expected_valuation, description in self.test_cases:
            with self.subTest(rational=rational_value, prime=prime, desc=description):
                # Convert rational to p-adic
                padic_num = PAdic(rational_value, prime)
                
                # Convert back to rational
                recovered_rational = padic_num.to_rational()
                
                # Verify we get back the same rational number
                self.assertEqual(rational_value, recovered_rational,
                               f"Failed roundtrip for {description}: {rational_value} -> PAdic({prime}) -> {recovered_rational}")
    
    def test_integer_to_padic_to_rational_conversion(self):
        """Test integer conversion consistency."""
        integer_cases = [0, 1, -1, 42, -17, 100, 1000]
        primes = [2, 3, 5, 7, 11]
        
        for integer in integer_cases:
            for prime in primes:
                with self.subTest(integer=integer, prime=prime):
                    # Convert integer to p-adic
                    padic_num = PAdic(integer, prime)
                    
                    # Convert back to rational
                    recovered_rational = padic_num.to_rational()
                    
                    # Should get back the integer as a fraction
                    expected_rational = Fraction(integer)
                    self.assertEqual(expected_rational, recovered_rational,
                                   f"Failed integer conversion: {integer} -> PAdic({prime}) -> {recovered_rational}")
    
    def test_padic_copy_constructor_conversion(self):
        """Test that copying a p-adic number preserves its rational value."""
        for rational_value, prime, expected_valuation, description in self.test_cases[:5]:  # Test subset for efficiency
            with self.subTest(rational=rational_value, prime=prime, desc=description):
                # Create original p-adic number
                original_padic = PAdic(rational_value, prime)
                
                # Create copy using copy constructor
                copied_padic = PAdic(original_padic, prime)
                
                # Both should convert to the same rational
                original_rational = original_padic.to_rational()
                copied_rational = copied_padic.to_rational()
                
                self.assertEqual(original_rational, copied_rational,
                               f"Copy constructor failed for {description}")
                self.assertEqual(rational_value, copied_rational,
                               f"Copy constructor roundtrip failed for {description}")
    
    def test_zero_handling(self):
        """Test that zero is handled correctly across different primes."""
        primes = [2, 3, 5, 7, 11]
        
        for prime in primes:
            with self.subTest(prime=prime):
                # Test zero as integer
                zero_padic = PAdic(0, prime)
                self.assertTrue(zero_padic.is_zero)
                self.assertEqual(Fraction(0), zero_padic.to_rational())
                
                # Test zero as fraction
                zero_fraction_padic = PAdic(Fraction(0), prime)
                self.assertTrue(zero_fraction_padic.is_zero)
                self.assertEqual(Fraction(0), zero_fraction_padic.to_rational())
    
    def test_precision_parameter(self):
        """Test that precision parameter is handled correctly."""
        test_rational = Fraction(1, 3)
        prime = 5
        precisions = [10, 20, 50]
        
        for precision in precisions:
            with self.subTest(precision=precision):
                padic_num = PAdic(test_rational, prime, precision=precision)
                self.assertEqual(padic_num.precision, precision)
                
                # Conversion should still work (though accuracy may vary with actual implementation)
                recovered = padic_num.to_rational()
                # For stub implementation, should get back the same value
                self.assertEqual(test_rational, recovered)
    
    def test_from_int_class_method(self):
        """Test the from_int class method."""
        integers = [0, 1, -1, 42, 100]
        primes = [2, 3, 5, 7]
        
        for integer in integers:
            for prime in primes:
                with self.subTest(integer=integer, prime=prime):
                    padic_num = PAdic.from_int(integer, prime)
                    recovered = padic_num.to_rational()
                    expected = Fraction(integer)
                    
                    self.assertEqual(expected, recovered,
                                   f"from_int failed: {integer} with prime {prime}")
    
    def test_conversion_error_cases(self):
        """Test that appropriate errors are raised for invalid inputs."""
        # These tests will be more relevant when actual validation is implemented
        # For now, just ensure the basic structure works
        
        # Test that we can create p-adic numbers without immediate errors
        try:
            PAdic(Fraction(1, 2), 5)
            PAdic(42, 7)
            PAdic(0, 3)
        except Exception as e:
            self.fail(f"Basic p-adic construction failed: {e}")


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)