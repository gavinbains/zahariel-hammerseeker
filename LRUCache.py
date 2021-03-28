# limited size, insert evicts oldest item (LRU)

"""
size 3
[1,2,3]

get 2
[2, 1, 3]

insert 4
[4, 2, 1]
"""

"""
Linked List
H         T
1 <-> 2 <-> 3
^ string values


Hash Table
{ value : index  }

"""

def get(value):
  map[value]: node 


class Node:
  def __str__(self):
    return str(self.value)

  def __repr__(self):
    return str(self.value)

  def __init__(self, val):
    self.value = val;
    self.next = None
    self.prev = None


class LRU:
  def __init__(self, maxSize):
    self.head = None
    self.tail = None
    # map will values -> node in the linkedList
    self.map = {}
    # max size possible for LRU
    self.currSize = 0
    self.maxSize = maxSize;

  def insert(self, value):

    # isnert here
    nodeToInsert = Node(value)
    if self.currSize == self.maxSize:
      """
      [1 -> 2 -> 3]
      get prev of self.tail, remove the next of that prev
      self.tail = prev
      """
      print('DID I GET HERE?')
      # evict tail set new tail
      tailPrev = self.tail.prev
      print(tailPrev.value)
      tailPrev.next = None
      del self.map[self.tail.value]
      del self.tail
      self.tail = tailPrev
    else:
      self.currSize += 1

    """
    [1 -> 2 -> 3]
    self.head prev to be nodeToInser
    set nodeToInser next as self.head
    set nodeToInsert as self.head
    """
    # insert at head
    if self.head:
      self.head.prev = nodeToInsert
      nodeToInsert.next = self.head
      self.head = nodeToInsert
    else:
      self.head = nodeToInsert
      self.tail = nodeToInsert
      self.currSize = 1

    # put in map
    self.map[value] = nodeToInsert
    return True

  def get(self, value):
    # get here
    try:
      return self.map[value]
    except KeyError:
      return 'THAT WAS REMOVED!!!'



def main():
  lru = LRU(3)
  lru.insert(1)
  lru.insert(2)
  lru.insert(3)

  print(lru.get(1))
  print(lru.get(2))
  print(lru.get(3))

  lru.insert(4)
  print(lru.get(4))
  print(lru.get(1))

main()



