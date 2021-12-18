class PCScreen:
  def __init__(self, screensize):
    self.ScreenSize = screensize

  def message(self):
    print('You selected screen with', self.ScreenSize, 'inches')