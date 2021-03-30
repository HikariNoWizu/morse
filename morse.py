# morse.py
# pylint: disable=missing-docstring

def decode_one_letter(letter):
    morse_dict = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
                  "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
                  "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
                  "-.--": "Y", "--..": "Z"}
    return morse_dict.get(letter, "")


def decode(message):
    return ''.join(list(map(decode_one_letter, message.split(' '))))
