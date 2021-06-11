
from lib.button_controller import BUTTON_CONTROLLER
from lib.led_controller import LED_CONTROLLER
from lib.encoder import ENCODER


# index 0 button = index 0 led
led_pins = [0,1,2,3,4]
button_pins = [5,6,7,8,9,10]
encoder_pins = [11,12]

leds = LED_CONTROLLER(led_pins)
buttons = BUTTON_CONTROLLER(button_pins, leds) # pass in leds object so buttons can control leds and their indexes match
knob = ENCODER(encoder_pins, leds, buttons.function_state)

while True:
  knob.check()
  buttons.check()
  leds.shineOn()
