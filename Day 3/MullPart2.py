import re

def analyze_memory():
    """
    Reads a file containing corrupted memory, extracts valid mul instructions, 
    and computes the sum of their results.
    """

        # Open and read the file content
    with open("Day 3/MullData.txt", 'r') as file:
            corrupted_memory = file.read()
        
    # Regular expression parsing to match valid mul instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do = r"(do\(\))"
    dont = r"(don't\(\))"
    # Added do and don't regular expressions to capture

    # Find all matches of the valid mul instructions
    matches = re.findall(pattern, corrupted_memory)
    do_matches = re.findall(do, corrupted_memory)
    dont_matches = re.findall(dont, corrupted_memory)
    print(matches)
    print(do_matches)
    print(dont_matches)
        
    # Compute the sum of the results of valid mul instructions
    #result_sum = sum(int(x) * int(y) for x, y in matches)

    #print(result_sum)

analyze_memory()
