from machine import UART

class DATA:
  def __init__(self, leds, buttons, knob):
    self.leds = leds
    self.buttons = buttons.buttons
    print('data init')

  def process(self):
    for button in self.buttons:
      if button.isPressed():
        print(button.index)