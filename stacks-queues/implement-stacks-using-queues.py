class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        for i in range(len(self.queue)-1):
            tmp = self.queue.pop(0)
            self.queue.append(tmp)
        self.queue.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        for i in range (len(self.queue)):
            tmp = self.queue.pop(0)
            self.queue.append(tmp)
        return tmp

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue:
            return False
        return True
        