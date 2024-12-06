import re

def analyze_memory():
    """
    To capture multiple strings in the order of occurance in the txt file, use "|" which means "or". In this context, if you use it on multiple patterns,
    it will go mul|do|dont, creating a big pattern that contains all of them yet seperate.
    """

        # Open and read the file content
    with open("Day 3/MullData.txt", 'r') as file:
        corrupted_memory = file.read()
        
    # Regular expression parsing to match valid mul instructions
    mul = r"mul\((\d{1,3}),(\d{1,3})\)"
    do = r"(do\(\))"
    dont = r"(don't\(\))"
    # Added do and don't regular expressions to capture

    patterns_to_match = [do, dont, mul]
    pattern = '|'.join(patterns_to_match)


    matches = re.findall(pattern, corrupted_memory)
    print(matches)

analyze_memory()
