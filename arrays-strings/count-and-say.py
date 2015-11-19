class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        curr = "1"
        seqs = 1
        
        while seqs < n:
            repeat_count = 1
            string = ""

            for i in range(1, len(curr)):
                if curr[i] == curr[i-1]:
                    repeat_count += 1

                else:
                    string += str(repeat_count)
                    string += curr[i-1]
                    repeat_count = 1
            
            string += str(repeat_count)
            string += curr[-1]
            curr = string
            seqs +=1
            
        return curr
        
        