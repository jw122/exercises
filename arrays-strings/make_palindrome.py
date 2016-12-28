
def make_palindrome(string):
    result = ""

    if not string:
        return None
    if len(string) == 1:
        return string
    string = list(string)
    count = 0
    while len(string) > 1: # O(n)
        char = string[0]
        del string[0]
        if char in string:        
            result = char + result
            result += char
            string.remove(char)
        elif char not in string and count == 0:
            string.append(char)
            count += 1
        else:
            return None
    if len(string) == 1:
        mid = len(result)/2
        result = result[:mid] + str(string[0]) + result[mid:]
    
    return result

print(make_palindrome("cattaco")) 
print(make_palindrome("coattac"))     
print(make_palindrome("apple"))
print(make_palindrome("ebb"))
print(make_palindrome("a"))
print(make_palindrome("bbaa"))