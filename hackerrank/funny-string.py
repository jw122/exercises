import fileinput

my_input = []
for line in fileinput.input():
    my_input.append(line.strip())
    
#NOTE: there is definitely a better way of doing this without having to reverse the entire string and compare.
#For example, one could iterate from different ends of the same string and check if the differences are the same.

def reverseString(string):
    s = list(string)
    last_index = len(s)-1
    i = 0
    mid = len(s)/2
    while (i < mid):
        curr = s[i]
        last = s[last_index - i]
        s[i] = last
        s[last_index-i] = curr
        i+=1
    string = ("").join(s)
    return string
        
def testFunny(string):
    string2 = reverseString(string)
    p1 = 0
    p2 = 1
    while(p2 < len(string)):
        
        if(abs(ord(string[p1]) - ord(string[p2]))!=abs(ord(string2[p1]) - ord(string2[p2]))):
            return "Not Funny"
        p1+=1
        p2+=1
    return "Funny"

for i in range(1, int(my_input[0])+1):
    print testFunny(my_input[i])