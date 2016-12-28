# Julia Wu, October 2016
# Execute this script by running 'python dictionary_dash.py'
import re
import unittest

class WordNode(object):
    def __init__(self, word):
        self.val = word
        self.prev = None

# Given two words (start and end) and the dictionary, find the length of the shortest transformation
# sequence from start to end
def shortest_transformation(start, end, dictionary):
    dictionary = [WordNode(w) for w in dictionary if w != start]
    start = WordNode(start)
    options = [start]
    final = None

    while len(options) > 0:
        curr = options.pop(0)

        if curr.val == end:
            final = curr
            break

        for i in range(len(curr.val)):
            if i == 0:
                pattern = '.' + curr.val[i+1:]
            else:
                pattern = curr.val[:i] + '.' + curr.val[i+1:]

            for word in dictionary:
                res = re.match(pattern, word.val)
                if res:
                    option = WordNode(res.group(0))
                    options.append(option)
                    option.prev = curr
                    dictionary = [w for w in dictionary if w.val != option.val]
    if final:
        path = []
        while final.prev:
            path.append(final.val)
            final = final.prev
        return len(path)
    else:
        return "No transformations found."

# TESTS!
class TestDictionaryDash(unittest.TestCase):

    def tests(self):
        # Expect hit -> hot -> dot -> dog -> cog (4)
        self.assertEqual(shortest_transformation("hit", "cog", ["hit", "dot", "dog", "cog", "hot", "log"]), 4)
        # Expect home -> hose -> pose -> post -> past (4)
        self.assertEqual(shortest_transformation("home", "past", ["home", "dome", "dose", "rose", "pose", "pose", "post", "past", "dame", "rise", "hose", "pest"]), 4)
        # Expect has -> his -> hit -> pit -> pet (4)
        self.assertEqual(shortest_transformation("has", "pet", ["hit", "has", "pot", "pet", "his", "pit", "sit", "pie"]), 4)
        # Expect invalid, since no transformations are possbile
        self.assertEqual(shortest_transformation("one", "two", ["win", "who"]), "No transformations found.")
        # Expect invalid, since dictionary is empty
        self.assertEqual(shortest_transformation("hi", "my", []), "No transformations found.")

if __name__ == '__main__':
    unittest.main()