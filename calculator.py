import sys

def calculate(num1, operator, num2):
    num1 = float(num1)
    num2 = float(num2)
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <num1> <operator> <num2>")
    else:
        result = calculate(sys.argv[1], sys.argv[2], sys.argv[3])
        print(result)