class Solution(object):

    def letter_combinations(self, inpt):
        phone_keys = {"2": "abc", "3": "def", 
        "4":"ghi", "5":"jkl", 
        "6":"mno", "7":"pqrs", 
        "8":"tuv", "9":"wxyz"}

        charsList = []
        for char in inpt:
            charsList.append(phone_keys[char])

        # print charsList

        res = self.helper(charsList, charsList[-1], len(charsList) - 2)
        # print res

    def helper(self, inputString, str2, index):
        print inputString
        str1 = inputString[index]
        res = []
            
        for char1 in str1:
            for char2 in str2:

                combo = char1 + char2
                res.append(combo)


        if index > 0:
            index -= 1
        
            self.helper(inputString, res, index)

        else:
            # print res
            return res


sol = Solution()
sol.letter_combinations("234")