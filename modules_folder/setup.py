# Databricks notebook source
#!/usr/bin/env python3

# Exported function
def as_int(a):
    return int(a)

# Exported function
def as_float(a):
    return float(a)

# Test function for module  
def _test():
    assert as_int('1') == 1

if __name__ == '__main__':
    _test()
