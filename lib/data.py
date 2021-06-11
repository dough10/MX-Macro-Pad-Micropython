from machine import UART

class data:
  def __init__(self):
    self.uart = UART(1, 9600)

    print('data init')