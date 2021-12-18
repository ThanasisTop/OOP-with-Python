class PCTower:
  def __init__(self, memorysize, frequency):
    self.MemorySize = memorysize
    self.Frequency = frequency
  
  def message(self):
    print('You selected PC Tower with memory:', self.MemorySize, 'GB and Frequency', self.Frequency, 'GHz' )
	