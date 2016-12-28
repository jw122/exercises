class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        p1 = len(a) -1
        p2 = len(b) - 1
        carry = 0
        res = "" 
        while p1 and p2 >= 0:
            if (a[p1] == "1" and b[p2] == "0") or (a[p1] == "0" and b[p2] == "1"):
                if carry > 0:
                    res = "0" + res
                else:
                    res = "1" + res
            elif (a[p1] == "1" and b[p2] == "1"):
                if carry > 0:
                    res = "1" + res
                else:
                    res = "0" + res
                    carry = 1
            elif (a[p1] == "0" and b[p2] == "0"):
                if carry > 0:
                    res = "1" + res
                    carry = 0
                else:
                    res = "0" + res
            p1 -= 1
            p2 -= 1
        
        if p1 >= 0:
            while p1 >= 0:
                if a[p1] == "1":
                    if carry > 0:
                        res = "0" + res
                    else:
                        res = "1" + res
                if a[p1] == "0":
                    if carry > 0: 
                        res = "1" + res
                    else:
                        res = "0" + res
                p1 -= 1
        if p2 >= 0:
            print p2
            while p2 >= 0:
                if b[p2] == "1":
                    if carry > 0:
                        res = "0" + res
                    else:
                        res = "1" + res
                if b[p2] == "0":
                    if carry > 0: 
                        res = "1" + res
                    else:
                        res = "0" + res
                p2 -= 1
        if carry:
            res = "1" + res
        print res