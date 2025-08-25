# P-adic Arithmetic Library

A Python library for exploring and computing with p-adic numbers, designed to provide a deeper understanding of this fascinating area of number theory through hands-on implementation and experimentation.

## What are P-adic Numbers?

P-adic numbers are a fundamental concept in modern number theory that provide an alternative way of measuring the "size" of numbers. While we're familiar with the usual absolute value (where |5| = 5 and |-3| = 3), p-adic numbers use a completely different notion of distance based on divisibility by a prime number p.

For a prime number p, the p-adic absolute value |x|_p of a rational number x is defined as follows:
- If x = 0, then |x|_p = 0
- If x = p^k × (a/b) where a and b are not divisible by p, then |x|_p = p^(-k)

This means that numbers are "small" in the p-adic metric when they are highly divisible by p. For example, in the 2-adic numbers:
- |8|_2 = 1/8 because 8 = 2³ × 1
- |3|_2 = 1 because 3 is not divisible by 2
- |1/2|_2 = 2 because 1/2 = 2^(-1) × 1

This seemingly strange metric leads to a rich mathematical structure where sequences can converge in unexpected ways, and where every non-zero p-adic number has a unique infinite series representation. P-adic numbers have applications in algebraic number theory, algebraic geometry, cryptography, and even in some areas of theoretical physics.

## Purpose of This Repository

This repository aims to:

1. **Educational Understanding**: Implement p-adic arithmetic from first principles to gain intuitive understanding of how these numbers work
2. **Computational Exploration**: Provide tools to experiment with p-adic numbers, visualize their properties, and explore mathematical relationships
3. **Learning Through Code**: Bridge the gap between abstract mathematical theory and concrete computational implementation
4. **Research Platform**: Serve as a foundation for exploring advanced topics in p-adic analysis and number theory

The library will implement core operations including:
- P-adic arithmetic (addition, multiplication, division)
- P-adic absolute values and metrics
- Conversion to/from regular rational numbers
- Hensel lifting for finding p-adic roots
- Series expansions and convergence
- Visualization tools for p-adic sequences and functions

## License

MIT License

Copyright (c) 2024 P-adic Arithmetic Library

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
