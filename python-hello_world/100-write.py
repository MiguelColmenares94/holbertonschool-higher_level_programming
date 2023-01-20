#!/usr/bin/python3
import sys

def print_to_stderr(*str):
    
    print(*str, file = sys.stderr)
    
    exit(1)

print_to_stderr("and that piece of art is useful - Dora Korpar, 2015-10-19")
