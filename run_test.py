#!/usr/bin/env python3
"""
Script to run individual test methods from the p-adic test suite.

Usage:
    python run_test.py <test_method_name>
    python run_test.py --list
    python run_test.py --help

Examples:
    python run_test.py test_zero_handling
    python run_test.py test_rational_to_padic_to_rational_conversion
"""

import sys
import unittest
from test_padic_conversion import TestPAdicConversion


def get_available_tests():
    """Get list of available test methods."""
    test_methods = []
    for attr_name in dir(TestPAdicConversion):
        if attr_name.startswith('test_'):
            test_methods.append(attr_name)
    return sorted(test_methods)


def run_specific_test(test_name):
    """Run a specific test method."""
    try:
        # Create test suite with just the specified test
        suite = unittest.TestSuite()
        test_instance = TestPAdicConversion(test_name)
        suite.addTest(test_instance)
        
        # Run the test
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        # Return success status
        return result.wasSuccessful()
        
    except Exception as e:
        print(f"Error running test '{test_name}': {e}")
        return False


def show_usage():
    """Show usage information."""
    print(__doc__)
    print("\nAvailable test methods:")
    for test_name in get_available_tests():
        print(f"  - {test_name}")


def main():
    """Main function."""
    if len(sys.argv) != 2:
        show_usage()
        return 1
    
    arg = sys.argv[1]
    
    if arg in ['--help', '-h']:
        show_usage()
        return 0
    
    if arg in ['--list', '-l']:
        print("Available test methods:")
        for test_name in get_available_tests():
            print(f"  - {test_name}")
        return 0
    
    test_name = arg
    available_tests = get_available_tests()
    
    if test_name not in available_tests:
        print(f"Error: Test method '{test_name}' not found.")
        print("\nAvailable test methods:")
        for test in available_tests:
            print(f"  - {test}")
        return 1
    
    print(f"Running test: {test_name}")
    print("=" * 50)
    
    success = run_specific_test(test_name)
    
    if success:
        print(f"\n✓ Test '{test_name}' passed!")
        return 0
    else:
        print(f"\n✗ Test '{test_name}' failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())