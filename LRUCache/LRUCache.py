# https://leetcode.com/problems/lru-cache
# T: O(1) and S: O(capacity)

class DLinkedNode():
	def __init__(self):
		self.key = 0
		self.value = 0
		self.prev = None
		self.next = None

class LRUCache(object):
	def __init__(self, capacity):
		self.cache = {}
		self.capacity = capacity
		self.size = 0
		self.head, self.tail = DLinkedNode(), DLinkedNode()
	
	def get(self, key):
		node = self.cache.get(key, None)
		if not node:
			return -1
		self._move_to_head(node)
		return node.value
	
	def _move_to_head(self, node):
		self._remove_node(node)
		self._add_node(node)
	
	def _remove_node(self, node):
		prev = node.prev
		new  = node.next

		prev.next = new
		new.prev = prev
	
	def _add_node(self, node):
		node.prev = self.head
		node.next = self.head.next
		
		self.head.next.prev = node
		self.head.next = node
	
def _pop_tail():
	res = self.tail.prev
self_remove_node(res)
return res	

	def put(self, key, value):
		node = self.cache.get(key)

		if not node:
			newNode = DLinkedNode()
			newNode.key = key
			newNode.value = value
			
			self.cache[key] = newNode
			self._add_node(newNode)
			self.size+=1
			if self.size > self.capacity:
				tail = self._pop_tail()
				del self.cache[tail.key]
				self.size-=1
		else:
			node.value = value
			self._add_node(node)
