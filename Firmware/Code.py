print("Starting")

# KMK Firmware Configuration File

# Import necessary modules from KMK and board library
import board

from kmk.modules.encoder import EncoderHanlder
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Define the keyboard matrix configuration and encoder pins

# Define column and row pins for the keyboard matrix
keyboard.col_pins = (board.GP3, board.GP4, board.GP5,) # Columns pins 
keyboard.row_pins = (board.GP7, board.GP6, board.GP2,) # Rows pins
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Configure the encoder module
encoder_handler = EncoderHanlder()

encoder_handler.pins = (
    (board.GP9, board.GP9, None), # Encoder 1 pins A and B
    (board.GP11, board.GP10, None), # Encoder 2 pins A and B
)

# Map encoder actions to keycodes
encoder_handler.map = [
    (KC.VOLD, KC.VOLU),  # Encoder 1: Volume Down/Up
    (KC.BRIU, KC.BRID),  # Encoder 2: Brightness Up/Down
]

keyboard.modules.append(encoder_handler)

# Define the keymap for the keyboard
keyboard.keymap = [
    [KC.1, KC.2, KC.3,
     KC.4, KC.5, KC.6,
     KC.7, KC.8, KC.9
    ],
]

if __name__ == '__main__':
    keyboard.go()