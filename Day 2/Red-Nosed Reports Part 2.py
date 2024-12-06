def input_reader():
    report_input = []
    with open('Input2024Day2.txt') as file:
        for line in file:
            report_value = [int(item) for item in line.strip().split()]
            report_input.append(report_value)
    return report_input

# Create a separate function that checks whether each line (aka item) is safe.
def is_safe(report):
    """Check if a report is safe based on the original rules."""
    increasing = True
    decreasing = True

    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1]) # Previous part, I had report[i] and i+1 in variables to better understand the logic.
        if diff not in [1, 2, 3]:
            return False # Previous part, instead of using a boolean to return if difference more than 3 and less than 1, I used a variable and set it to 0 for unsafe and 1 for safe.
        if report[i] > report[i + 1]:
            increasing = False
        if report[i] < report[i + 1]:
            decreasing = False

    return increasing or decreasing # Returns true when it is increasing or decreasing, and false when neither or both.


def safety_with_dampener(report_input):
    safe_count = 0
    "For each line in the report_input list..."
    for item in report_input:
        # Check if the report is already safe
        if is_safe(item):
            safe_count += 1
            continue

        # Try removing each level and check if it becomes safe
        for i in range(len(item)):
            modified_item = item[:i] + item[i + 1:]  # Creates new list by adding the elements before element of i, excluding element of i, with the elements of i+1 and above.
            if is_safe(modified_item):
                safe_count += 1
                break  # No need to check further; one removal is enough

    print(safe_count)


# Read the input and process the reports
report_input = input_reader()
safety_with_dampener(report_input)
