from lib.rotary_irq_rp2 import RotaryIRQ

class ENCODER: 
  def __init__(self, pins, leds, __function_state):
    self.__knob = RotaryIRQ(
      pin_num_clk=pins[0],
      pin_num_dt=pins[1],
      min_val=0,
      max_val=65025,
      reverse=False,
      range_mode=RotaryIRQ.RANGE_UNBOUNDED,
      pull_up=True)
    self.__value = self.__knob.value()
    self.__function_state = __function_state
    self.LEDS = leds

  def check(self):
    newVal = self.__knob.value()
    if newVal != self.__value:
      if newVal > self.__value:
        if self.__function_state[0]:
          if self.LEDS.brightness > 0 and self.LEDS.mode == 0:
            self.LEDS.brightness -= 4335
            print(self.LEDS.brightness)
        else :
          print('up')
      if newVal < self.__value:
        if self.__function_state[0]:
          if self.LEDS.brightness < 65025 and self.LEDS.mode == 0:
            self.LEDS.brightness += 4335
            print(self.LEDS.brightness)
        else :
          print('down')
      self.__value = newVal
      print('')