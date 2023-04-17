import winsound
import time

# Define the Morse code dictionary
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def convert_to_morse(text):
    morse_code = ""
    for letter in text:
        if letter.upper() in morse_dict:
            morse_code += morse_dict[letter.upper()] + " "
        elif letter == " ":
            morse_code += "/ "
    return morse_code

def play_morse_code(morse_code):
    for letter in morse_code:
        if letter == ".":
            winsound.Beep(400, 130)
            time.sleep(0.05)
        elif letter == "-":
            winsound.Beep(500, 300)
            time.sleep(0.05)
        elif letter == "/":
            time.sleep(0.1)
        elif letter == " ":
            time.sleep(0.2)

# Prompt the user for input
text = input("Enter text to convert to Morse code: ")

# Convert the text to Morse code
morse_code = convert_to_morse(text)

# Play the Morse code as sound
play_morse_code(morse_code)
