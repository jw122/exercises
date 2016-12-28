# Complete the function below.

encrypted_message = "Atvt hrqgse, Cnikg"

def decrypt(encrypted_message):

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # key = "2512208"
    # key = "8022152"
    key = "5122082"
    keyIndex = 6
    result = ""
    for i in range(len(encrypted_message)-1,-1,-1):
        
        letter = encrypted_message[i]
        print letter
        if not letter.isalnum():
            result = letter + result
            continue

        letterIndex = alphabet.index(letter.lower())
        shiftCount = int(key[keyIndex])
        keyIndex -= 1
        if letterIndex - shiftCount < 0:
            actualLetter = alphabet[26 + (letterIndex-shiftCount)]
            if letter.isupper():
                result = actualLetter.upper() + result
            else:
                result = actualLetter + result
        else:
            actualLetter = alphabet[letterIndex - shiftCount]
            if letter.isupper():
                result = actualLetter.upper() + result
            else:
                result = actualLetter + result

        if keyIndex == 0:
            keyIndex = 6
    print result

# def  decrypt(encrypted_message):
#     alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     key = "2512208"
#     keyIndex = 0
#     result = ""
#     for letter in encrypted_message:
#         if not letter.isalnum():
#             result += letter
#             continue
#         print letter
#         if keyIndex == 7:
#             keyIndex = 0

#         letterIndex = alphabet.index(letter.lower())
#         shiftCount = int(key[keyIndex])
#         keyIndex += 1
#         if letterIndex - shiftCount < 0:
#             actualLetter = alphabet[26 + (letterIndex-shiftCount)]
#             if letter.isupper():
#                 result += actualLetter.upper()
#             else:
#                 result += actualLetter
#         else:
#             actualLetter = alphabet[letterIndex - shiftCount]
#             if letter.isupper():
#                 result += actualLetter.upper()
#             else:
#                 result += actualLetter
#     print(result)

            
decrypt(encrypted_message)