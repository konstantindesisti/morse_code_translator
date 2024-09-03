from morse_mapping import morse_code
from sound_manager import SoundCreator

user_input = list(input('Enter text you need to convert to Morse Code: ').upper())
speed_input = float(input('Enter desired speed: '))


def converter():
    """
    Translates given sentence into a morse code without spaces.
    :return: List of translated letters
    """
    try:
        translated_word = ''
        for symbol in user_input:
            translated_word += (morse_code[symbol])
            translated_word += ' '
        return translated_word
    except KeyError:
        print('Please use valid keys: A-Z and 0-9')


converted_text = converter()
sound_play = SoundCreator()
sound_play.player(converted_text)
print(converted_text)
