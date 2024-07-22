import re

def add(numbers):
    if not numbers:
        return 0

    delimiter, numbers = extract_delimiter(numbers)
    number_list = split_numbers(numbers, delimiter)
    
    return sum_numbers(number_list)

def extract_delimiter(numbers):
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter_part = parts[0][2:]
        numbers = parts[1]
        
        if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
            delimiter = re.escape(delimiter_part[1:-1])
        else:
            delimiter = re.escape(delimiter_part)
    else:
        delimiter = ","
        
    return delimiter, numbers

def split_numbers(numbers, delimiter):
    return re.split(f"{delimiter}|\n", numbers)

def sum_numbers(number_list):
    total = 0
    negatives = []
    
    for number in number_list:
        if number:
            num = int(number)
            if num < 0:
                negatives.append(num)
            elif num <= 1000:
                total += num
    
    if negatives:
        raise ValueError(f"negatives not allowed: {negatives}")
    
    return total
