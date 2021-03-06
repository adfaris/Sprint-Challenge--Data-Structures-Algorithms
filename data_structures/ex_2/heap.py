def heapsort(arr):
  heap = Heap()
  sorted = [0] * len(arr)

  for i in arr:
    heap.insert(i)

  for i in range(len(arr)):
    sorted[len(arr)-i-1] = heap.delete()

  return sorted

  # def heapsort(arr):
  # heap = Heap()
  # for each in arr:
  #   heap.insert(each)

  # while heap.size > 0:
  #   max_val = heap.storage[1]
  #   heap.storage[1] = heap.storage[heap.size]
  #   heap.storage[heap.size] = max_val
  #   heap.size -= 1
  #   heap._sift_down(1)

  # return heap.storage[1:]
# This javascript code should work but wasn't able to convert it to python. 
# let heap = new Heap()
# const sorted = new Array(arr.length)
# for(let i =0 ; i < arr.length; i++){
#   heap.insert(arr[i])
# }
# for(let i= arr.length-1; i < -1; i++){
#   sorted[i] = heap.delete()
# }
# return sorted


class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    retval = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return retval

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index // 2] < self.storage[index]:
        self.storage[index], self.storage[index // 2] = self.storage[index // 2], self.storage[index]
      index = index // 2

  def _sift_down(self, index):
    while (index * 2) <= self.size:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1