def input_reader():
    report = []
    with open("Input2024Day2.txt") as file:
        for line in file:
            report_value = []
            for item in line.strip().split(): # First, the line is splitting each item by identifying the spaces, and turns each item into its own seperate list. 
                # It then removes/strips any whitespace from the line.
                report_value.append(item)
            report.append(report_value)
        print(report)
        return report

#if item.isdigit():
#    report_value.append(item) 
# The code above can be put in place of the line.split()

def safety(report):
    safe_count = 0
    for item in report:
        if item[0] not in item[1:]:
    # This checks if item[0] is not equal to any of the remaining elements.
    # if item[0] != item[1, len(item)]: is incorrect
            for subitem in item:
                

        

report = input_reader()