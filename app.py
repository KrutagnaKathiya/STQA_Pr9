# app.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Deliberately cause a wrong calculation for testing
    return (a / b) + 1  # This will fail tests
