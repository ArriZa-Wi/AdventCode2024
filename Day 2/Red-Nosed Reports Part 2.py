def input_reader():
    report = []
    with open('Input2024Day2.txt') as file:
        for line in file:
            report_value = [int(item) for item in line.strip().split()]
            report.append(report_value)
    return report

# Create seperate function to check the safety conditions of each line.
def is_safe(levels):
    """Check if a report is safe based on the original rules."""
    increasing = True
    decreasing = True

    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff not in [1, 2, 3]:
            return False
        if levels[i] > levels[i + 1]:
            increasing = False
        if levels[i] < levels[i + 1]:
            decreasing = False

    return increasing or decreasing


def safety_with_dampener(report):
    safe_count = 0

    for item in report:
        # Check if the report is already safe
        if is_safe(item):
            safe_count += 1
            continue

        # Try removing each level and check if it becomes safe
        for i in range(len(item)):
            modified_item = item[:i] + item[i + 1:]  # Remove one level
            if is_safe(modified_item):
                safe_count += 1
                break  # No need to check further; one removal is enough

    print(safe_count)


# Read the input and process the reports
report = input_reader()
safety_with_dampener(report)
