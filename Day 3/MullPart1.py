import re

def analyze_memory(file_path):
    """
    Reads a file containing corrupted memory, extracts valid mul instructions, 
    and computes the sum of their results.
    """

        # Open and read the file content
    with open("Day 3/MullData.txt", 'r') as file:
            corrupted_memory = file.read()
        
    # Regular expression parsing to match valid mul instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    # () that arent followed by a \ are capture groups. Whatever is inside, will be taken as the parts that will be looked for in the txt file.
    # When \ and the element after is light orange, it means the char after is literal.
    # \d means digit. {} is how many digits it takes. More than 1, and up to 3 digits within the () group.
    
    # Find all matches of the valid mul instructions
    matches = re.findall(pattern, corrupted_memory)
    full_matches = [f"mul({x},{y})" for x, y in matches] # to store entire mul(x,y) format into the list.
    print(full_matches)
        
    # Compute the sum of the results of valid mul instructions
    result_sum = sum(int(x) * int(y) for x, y in matches)
        
    return result_sum


# Example usage:
file_path = "corrupted_memory.txt"  # Replace with your file path
result = analyze_memory(file_path)
print(f"The sum of the results of valid mul instructions is: {result}")
