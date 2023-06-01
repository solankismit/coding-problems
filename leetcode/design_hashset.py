class MyHashSet(object):

    def __init__(self):
        self.hash = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in list(self.hash.keys()):
            self.hash[key]=1
        print(list(self.hash.keys()))

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in list(self.hash.keys()):
            self.hash.__delitem__(key)
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in list(self.hash.keys())

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(2)
obj.add(2)
obj.remove(2)
obj.add(3)
print(obj.contains(3))
# param_3 = obj.contains(2)