import re

def add(numbers):
    if not numbers:
        return 0
    
    delimiter = ","
    
    # Support for custom delimiters of any length
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter_part = parts[0][2:]
        numbers = parts[1]
        
        if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
            delimiter = re.escape(delimiter_part[1:-1])
        else:
            delimiter = re.escape(delimiter_part)
    
    numbers = re.split(f"{delimiter}|\n", numbers)
    
    total = 0
    negatives = []
    
    for number in numbers:
        if number:
            num = int(number)
            if num < 0:
                negatives.append(num)
            elif num <= 1000:
                total += num
    
    if negatives:
        raise ValueError(f"negatives not allowed: {negatives}")
    
    return total
