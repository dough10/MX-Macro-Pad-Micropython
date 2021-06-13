from machine import Pin, PWM

class LED_CONTROLLER:
  def __init__(self, pins):
    self.LEDS = []
    self.brightnesses = []
    self.mode = 0
    self.keyPressed = False
    self.brightness = 0
    self.__currentLED = 1
    self.__krIncriment = 765
    self.__krBrightness = 65025 - self.__krIncriment
    self.__changeBy = -1
    self.__clickIncriment = 25
    self.__breathIncriment = 9
    self.__breathBrightness = 0
    for pin in pins:
      pwm = PWM(Pin(pin))
      pwm.freq(1000)
      pwm.duty_u16(65025)
      self.LEDS.append(pwm)
      self.brightnesses.append(65025)

  def setMode(self, mode):
    self.mode = mode

  def shineOn(self):
    if self.mode == 0:
      self.__variableBrightness()
    if self.mode == 1:
      self.__onPressMode()
    if self.mode == 2:
      self.__breath()
    if self.mode == 3:
      self.__KnightRider()
    if self.mode == 4:
      self.__off()

  def __off(self):
    for led in self.LEDS:
      led.duty_u16(-2)

  def __variableBrightness(self):
    for led in self.LEDS:
      led.duty_u16(self.brightness)

  def __breath(self):
    for led in self.LEDS:
      led.duty_u16(self.__breathBrightness)
    self.__breathBrightness = self.__breathBrightness + self.__breathIncriment
    if self.__breathBrightness <= 0 or self.__breathBrightness >= 65025:
      self.__breathIncriment = -self.__breathIncriment

  def __onPressMode(self):
    for num, brightness in enumerate(self.brightnesses, start=0):
      self.LEDS[num].duty_u16(self.brightnesses[num])
      if brightness < 65025 and not self.keyPressed:
        self.brightnesses[num] = self.brightnesses[num] + self.__clickIncriment

  def __KnightRider(self):
    self.LEDS[self.__currentLED].duty_u16(self.__krBrightness)
    if (self.__krBrightness >= 65025):
      self.__krIncriment = -self.__krIncriment
      if (self.__currentLED >= 4 or self.__currentLED <= 0):
        self.__changeBy = -self.__changeBy
      self.__currentLED = self.__currentLED + self.__changeBy
    if (self.__krBrightness <= 0):
      self.__krIncriment = -self.__krIncriment
    self.__krBrightness = self.__krBrightness + self.__krIncriment
    