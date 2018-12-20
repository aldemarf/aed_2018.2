

# Tabela hash com colisões resolvidas por encadeamento
# (Utilizado listas concretas do python)

from math import ceil, fmod, sqrt
class HashChainUnity:
	def __init__(self, key, value):
		self.__key = key
		self.__value = value
		self.__next = None

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

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self, newValue):
		self.__next = newValue


class HashTable:
	CONST = (1 + sqrt(5)) / 2 - 1
	PRIME = 1453


	def __init__(self, slots=1453):
		self.__size = slots
		self.__table = [None for a in range(slots)]


	def __9Hash__(self, key):
		address = fmod(key, 9)
		return address

	def __divisionHash__(self, key):
		address = fmod(key, self.PRIME)
		return address

	def __MultiplyHash__(self, key):
		address = ceil(self.PRIME * fmod(key * self.CONST, 1))
		return address


	@property
	def size(self):
		return self.__size

	@property
	def table(self):
		return self.__table

	@table.setter
	def table(self, hashValue, item):
		self.__table[hashValue] = item

	def sweepBucket(self, bucket, key):
		pass


	def insertValue(self, key, value):
		item = HashChainUnity(key, value)
		self.table = (self.__9Hash__(key), item)




################################################################
#							Exemplos						   #
################################################################


#########################
# CHAINED LINKED LIST

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



#########################
# LINEAR PROBING -- SPT

class HashTable:
	def __init__(self, size):
		self.size = size
		self.keys = [None] * self.size
		self.values = [None] * self.size

	def hash_function(self, key):
		return hash(key) % self.size

	def get_slot(self, key):
		slot = self.hash_function(key)
		while self.keys[slot] and self.keys[slot] != key:
			slot = self.hash_function(slot + 1)
		return slot

	def set(self, key, value):
		slot = self.get_slot(key)
		self.keys[slot] = key
		self.values[slot] = value

	def get(self, key):
		return self.values[self.get_slot(key)]



class HashTable:

	ratio_expand = .8
	ratio_shrink = .2
	min_size = 11

	def __init__(self, size=None):
		self._size = size or self.min_size
		self._buckets = [None] * self._size
		self._list = None
		self._count = 0

	def _entry(self, key):
		# get hash and index
		idx = hash(key) % self._size
		# find entry by key
		p, q = self._buckets[idx], None
		while p and p.key != key:
			p, q = p.next, p
		# index, entry, previous entry
		return idx, p, q
	def _ensure_capacity(self):
		fill = self._count / self._size

		# expand or shrink?
		if fill > self.ratio_expand:
			self._size = self._size * 2 + 1
		elif fill < self.ratio_shrink and \
				self._size > self.min_size:
			self._size = (self._size - 1) // 2
		else:
			return
		# reallocate buckets
		self._buckets = [None] * self._size
		# store entries into new buckets
		p = self._list
		while p:
			idx = hash(p.key) % self._size
			p.next = self._buckets[idx]
			self._buckets[idx] = p
			p = p.entry_next
	def __len__(self):
		return self._count
	def __contains__(self, key):
		_, p, _ = self._entry(key)
		return bool(p)
	def __getitem__(self, key):
		_, p, _ = self._entry(key)
		return p and p.value
	def __setitem__(self, key, value):
		idx, p, _ = self._entry(key)
		# set entry if key was found
		if p:
			p.value = value
			return
		# create new entry
		p = SimpleNamespace(
			key=key,
			value=value,
			next=self._buckets[idx],
			entry_next=self._list,
			entry_prev=None
		)
		# store to bucket
		self._buckets[idx] = p
		# store to list
		if self._list:
			self._list.entry_prev = p
		self._list = p
		# expand
		self._count += 1
		self._ensure_capacity()
	def __delitem__(self, key):
		idx, p, q = self._entry(key)
		# key not found
		if not p:
			return
		# remove from bucket
		if q:
			q.next = p.next
		else:
			self._buckets[idx] = p.next
		# remove from list
		if p.entry_next:
			p.entry_next.entry_prev = p.entry_prev
		if p.entry_prev:
			p.entry_prev.entry_next = p.entry_next
		else:
			self._list = p.entry_next
		# shrink
		self._count -= 1
		self._ensure_capacity()
	def __iter__(self):
		p = self._list
		while p:
			yield p.key
			p = p.entry_next

	def slots(self):
		return ''.join(p and 'x' or '-' for p in self._buckets)