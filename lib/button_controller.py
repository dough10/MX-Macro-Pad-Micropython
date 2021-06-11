from lib.button import Button

# places button objects in an array 
class BUTTON_CONTROLLER:
  def __init__(self, pins, leds):
    self.__buttons = []
    self.function_state = [
      False
    ]
    for index, pin in enumerate(pins, start=0):
      self.__buttons.append(Button(pin, leds, index, self.function_state))

  # checks all buttons in button array to see if they are pressed
  def check(self):
    for button in self.__buttons:
      button.update()