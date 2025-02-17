def add(x, y):
    try:
        return float(x) + float(y)
    except ValueError: 
        return "Error: Non-numeric input"
    
def subtract(x, y):
    try:
        return (float(x) - float(y))
    except ValueError:
        return "Error: Non-numeric input"
    
def multiply(x, y):
    try:
        return (float(x) * float(y))
    except ValueError:
        return "Error: Non-numeric input"
    
def divide(x, y):
    try:
        if float(y) == 0:
            return "Error: You cannot divide by 0"
        return (float(x) / float(y))
    except ValueError:
        return "Error: Non-numeric input"
    