

# Tabela hash com colisões resolvidas por encadeamento
# (Utilizado listas concretas do python)

class valuePair:
	def __init__(self, key, value):
		self.__key = key
		self.__value = value

	@property
	def key(self):
		return self.__key
	
	@key.setter
	def key(self, newKey):
		self.__key = newKey

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, newValue):
		self.__value = newValue
	
	@property
	def pair(self):
		return (self.key, self.value)

	@pair.setter
	def pair(self, newKey, newValue):
		self.__key = newKey
		self.__value = newValue


	


class HashTable:
	def __init__(self, slots=256):
		self.__size = slots
		self.__table = [None for a in range(slots)]
	

	def __9Hash__(self, key):
		address = key % 9
		return address

	@property
	def size(self):
		return self.__size


	def insertValue(self, value):
		
		for bucket in range(self.size):
			pass




################################################################
#							Exemplos						   #
################################################################

class HashEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	

class HashTable:
	def __init__(self, size):
		self.size = size
		self.table = [None] * self.size

	def hashing_function(self, key):
		return hash(key) % self.size

	def rehash(self, entry, key, value):
		while entry and entry.key != key:
			prev, entry = entry, entry.next
		if entry:
			entry.value = value
		else:
			prev.next = HashEntry(key, value)

	def set(self, key, value):
		slot = self.hashing_function(key)
		entry = self.table[slot]
		if not entry:
			self.table[slot] = HashEntry(key, value)
		else:
			self.rehash(entry, key, value)
	
	def get(self, key):
		hash = self.hashing_function(key)
		if not self.table[hash]: raise KeyError
		else:
			entry = self.table[hash]
			while entry and entry.key != key: entry = entry.next
			return entry.value


