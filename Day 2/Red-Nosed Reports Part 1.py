def input_reader():
    report = []
    with open('Input2024Day2.txt') as file:
        for line in file:
            report_value = []
            for item in line.strip().split(): # First, the line is splitting each item by identifying the spaces, and turns each item into its own seperate list. 
                # It then removes/strips any whitespace from the line.
                report_value.append(int(item)) # appends each while simultaneously converting them to integers
            report.append(report_value)
        print(report)
        return report

#if item.isdigit():
#    report_value.append(item) 
# The code above can be put in place of the line.split()

def safety(report):
    safe_count = 0
    
    for item in report:
        subitem_safe = 1
        increasing = True
        decreasing = True
        for subitem in range(len(item)-1):
            nth = item[subitem]
            second_nth = item[subitem+1]
            difference = abs(nth - second_nth)

            if difference not in [1, 2, 3]:
                subitem_safe = 0
                break

            if nth >= second_nth:
                increasing = False
            if nth <= second_nth:
                decreasing = False
        if subitem_safe == 1 and (increasing or decreasing):
            safe_count += 1
    print(safe_count)

report = input_reader()
safety(report)

