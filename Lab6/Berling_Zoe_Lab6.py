"""Zoe Berling Algorithms Lab 6 HashTable ADT with chaining implementation """

class MyHashtable(object):
    """sample code from lab doc"""
    def __init__(self, size): # Creates an empty hashtable
        self.size = size
        # Create the list (of size) of empty lists (chaining)
        self.table = []
        for i in range(self.size):
            self.table.append([])

    def __str__(self): # for print
        return str(self.table)

    def insert(self, elem): # Adds an element into the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].append(elem)

    def member(self, elem): # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size
        return elem in self.table[hash]

    def delete(self, elem): # Removes an element from the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].remove(elem)


class LPHashtable(object):
    """Hashtable with linear probing"""
    def __init__(self, size):
        self.size = size
        self.table = [None]*self.size
        self.status = ['empty']*self.size

    def insert(self, elem):
        """Insert element into table if there is no element in the space"""
        hash = ord(elem[0]) % self.size
        tries = 0
        while True:
            if self.status[hash] != 'filled':
                self.table[hash] = elem
                self.status[hash] = 'filled'
                return elem
            elif tries == self.size:
                return False
            else:
                if hash == self.size-1:
                    hash = (hash * -1) + (self.size-1)
                    tries += 1
                else:
                    hash += 1
                    tries += 1

    def member(self, elem): # Returns True if element exists in hashtable
        hash = ord(elem[0]) % self.size
        tries = 0
        while True:
            if self.status[hash] == 'empty':
                return False  # element does not exist in table
            elif self.table[hash] == elem:
                return elem in self.table[hash]
            elif tries == self.size:
                return False  # element does not exist in table
            else:
                if hash == self.size - 1:
                    hash = (hash*-1) + (self.size-1)
                    tries += 1
                else:
                    hash += 1
                    tries += 1

    def __str__(self):
        return str(self.table)

    def printstatus(self):
        print(str(self.status))

    def insert(self, elem):
        """Insert element into table if there is no element in the space"""
        hash = ord(elem[0]) % self.size
        tries = 0
        while True:
            if self.status[hash] != 'filled':
                self.table[hash] = elem
                self.status[hash] = 'filled'
                return elem
            elif tries == self.size:
                return False
            else:
                if hash == self.size-1:
                    hash = (hash * -1) + (self.size-1)
                    tries += 1
                else:
                    hash += 1
                    tries += 1

    def member(self, elem): # Returns True if element exists in hashtable
        hash = ord(elem[0]) % self.size
        tries = 0
        while True:
            if self.status[hash] == 'empty':
                return False  # element does not exist in table
            elif self.table[hash] == elem:
                return elem in self.table[hash]
            elif tries == self.size:
                return False  # element does not exist in table
            else:
                if hash == self.size - 1:
                    hash = (hash*-1) + (self.size-1)
                    tries += 1
                else:
                    hash += 1
                    tries += 1

    def delete(self, elem):
        """deletes element if it exists and changes status to deleted"""
        hash = ord(elem[0]) % self.size
        tries = 0
        while True:
            if self.status[hash] == 'empty':
                return False # element does not exist in table
            elif self.table[hash] == elem:
                self.table[hash] = None
                self.status[hash] = 'deleted'
                return elem
            elif tries == self.size:
                return False  # element does not exist in table
            else:
                if hash == self.size - 1:
                    hash = (hash*-1) + (self.size-1)
                    tries += 1
                else:
                    hash += 1
                    tries += 1


# Testing code
# s = LPHashtable(10)
# # s = MyHashtable(10)
# s.insert("amy") #97
# s.insert("chase") #99
# s.insert("chris") #99
# s.insert("cam")
# s.insert("a")
# s.insert("b")
# s.insert("f")
# s.insert("k")
# s.insert("kim")
# s.insert("james")
# s.insert("jamie")
# print(s)
# print(s.member("amy"))
# print(s.member("chris"))
# print(s.member("alyssa"))
# print(s.delete("chase"))
# s.insert("jamie")
# print(s.delete("amy"))
# print(s)
# print(s.member("chris"))
# s.insert('lauren')
# print(s.member('a'))
# s.delete('lauren')
# print(s.member('a'))
# print(s)
# s.printstatus()
# You can use print(s) at any time to see the contents
# of the t