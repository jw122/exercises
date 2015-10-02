import fileinput
my_input = fileinput.input()

total_levels = int(my_input[0])
curr_level = 1

while (curr_level < total_levels+1):
    string = [" "]*total_levels
    
    for i in range(1, curr_level+1):
        string[len(string)-i] = "#"
    print ("").join(string)
    curr_level = curr_level + 1