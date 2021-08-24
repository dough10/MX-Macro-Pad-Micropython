# mx-macro-pad-micropython V:1.0.1

rewrite of [MX-Macro-Pad](https://github.com/dough10/MX-Macro-Pad) for Arduino AVR in Micropython for the Raspberry pi Pico.

micropython doesn't currently have support for usb-hid on pi pico board atm. this project is bassicly boiler plate for when it is working.

## install

1. write files from src folder to your pico board
2. assign the pins for leds, buttons and encoder in main.py
3. plug up leds, buttons and encoder
4. watch lights blink and keypresses register in pico console

## Dependencies

No Dependencies

## Dev Dependencies

- jsdoc-to-markdown: ^7.0.1
- version-incrementer: ^0.1.1
