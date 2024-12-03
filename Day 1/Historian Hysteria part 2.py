def location_id():
    with open('Location IDs.txt') as file:
        left_list = []
        right_list = []
        for line in file:
            data = line.strip().split()
            left_list.append(data[0])
            right_list.append(data[1])
    return left_list, right_list  # Return both lists

def sort_left(left_list):
    for marker_a in range(1, len(left_list)):
        unsorted_value = left_list[marker_a]
        marker_b = marker_a
        # Move Marker B left to where unsorted value should go
        while marker_b > 0 and left_list[marker_b-1] > unsorted_value:
            # Shift elements to the right and move left
            left_list[marker_b] = left_list[marker_b-1]
            marker_b -= 1

        # Move unsorted value to correct spot
        left_list[marker_b] = unsorted_value

    print("Sorted left list:", left_list)

def sort_right(right_list):
    for marker_a in range(1, len(right_list)):
        unsorted_value = right_list[marker_a]
        marker_b = marker_a
        # Move Marker B left to where unsorted value should go
        while marker_b > 0 and right_list[marker_b-1] > unsorted_value:
            # Shift elements to the right and move left
            right_list[marker_b] = right_list[marker_b-1]
            marker_b -= 1

        # Move unsorted value to correct spot
        right_list[marker_b] = unsorted_value

    print("Sorted right list:", right_list)

def similarity(left_list, right_list):
    sim_score = 0
    for item in left_list:
        occurance = 0
        occurance += right_list.count(item)
        sim_score += int(item) * occurance
    print(sim_score)

# Call the functions
left_list, right_list = location_id()  # Get both lists
sort_left(left_list)                   # Sort and print the left list
sort_right(right_list)                 # Sort and print the right list
similarity(left_list, right_list)