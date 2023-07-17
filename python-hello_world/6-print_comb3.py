#!/usr/bin/python3

for tens_digit in range(10):
        print("{:02d}".format(tens_digit * 10 + units_digit), end=", " if tens_digit < 8 else "\n")
