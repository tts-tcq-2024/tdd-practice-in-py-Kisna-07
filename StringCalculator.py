import re

def add(numbers):
    if not numbers:
        return 0

    delimiter, numbers = extract_delimiter(numbers)
    number_list = split_numbers(numbers, delimiter)
    
    return calculate_sum(number_list)

def extract_delimiter(numbers):
    if numbers.startswith("//"):
        delimiter_part, numbers = split_custom_delimiter(numbers)
        delimiter = parse_custom_delimiter(delimiter_part)
    else:
        delimiter = ","
    return delimiter, numbers

def split_custom_delimiter(numbers):
    parts = numbers.split("\n", 1)
    return parts[0][2:], parts[1]

def parse_custom_delimiter(delimiter_part):
    if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
        return re.escape(delimiter_part[1:-1])
    return re.escape(delimiter_part)

def split_numbers(numbers, delimiter):
    return re.split(f"{delimiter}|\n", numbers)

def calculate_sum(number_list):
    total = 0
    negatives = []
    for number in number_list:
        if number:
            num = int(number)
            check_negative(num, negatives)
            total += include_number(num)
    handle_negatives(negatives)
    return total

def check_negative(num, negatives):
    if num < 0:
        negatives.append(num)

def include_number(num):
    return num if num <= 1000 else 0

def handle_negatives(negatives):
    if negatives:
        raise ValueError(f"negatives not allowed: {negatives}")
