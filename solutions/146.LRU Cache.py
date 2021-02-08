"""
Hashmap + doubly linked list
Most recently used node at head, Least recently used node at tail
Time complexity: O(1)
Space complexity: O(capacity)
"""
class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()

        self.dummyhead = Node(None, None)
        self.dummytail = Node(None, None)
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # remove node from linked list
            # add node at head
            # return node value

            node = self.hashmap[key]
            self.removeNode(node)
            self.addAtHeadNode(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # remove node from linked list
            # update node value
            # add node to head

            node = self.hashmap[key]
            self.removeNode(node)
            node.val = value
            self.addAtHeadNode(node)

        else:
            if len(self.hashmap) + 1 > self.capacity:
                # remove tail node in hashmap
                # remove tail node from linked list
                self.hashmap.pop(self.dummytail.prev.key)
                self.removeNode(self.dummytail.prev)

            # add node at head
            # add node to hashmap
            newNode = Node(key, value)
            self.addAtHeadNode(newNode)
            self.hashmap[key] = newNode

    def addAtHeadNode(self, curNode):
        tmp = self.dummyhead.next

        self.dummyhead.next, tmp.prev  = curNode, curNode
        curNode.next, curNode.prev = tmp, self.dummyhead

    def removeNode(self, curNode):
        curNode.prev.next, curNode.next.prev= curNode.next, curNode.prev
        del curNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
