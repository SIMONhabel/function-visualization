import numpy as np

def linear(x, a=1, b=0):
    return a * x + b

def quadratic(x, a=1, b=0, c=0):
    return a * x**2 + b * x + c

def sine(x, amp=1, freq=1):
    return amp * np.sin(freq * x)

def exponential(x, a=1):
    return a * np.exp(x)

def absolute(x):
    return np.abs(x)