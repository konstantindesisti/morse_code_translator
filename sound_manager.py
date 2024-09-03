from pathlib import Path
from sys import stderr

from pydub import AudioSegment
from pydub.playback import play


def get_sound_file_path(sound_file):
    current_directory = Path.cwd()
    sound_file_path = current_directory / 'sounds' / sound_file
    return sound_file_path


class SoundCreator:
    def __init__(self):
        self.dit_sound = AudioSegment.from_file(get_sound_file_path('dit.mp3'), format='mp3')
        self.duh_sound = AudioSegment.from_file(get_sound_file_path('duh.mp3'), format='mp3')
        self.intra_space_sound = AudioSegment.from_file(get_sound_file_path('intra_space.mp3'), format='mp3')

    def player(self, converted_text):
        output_sound_file = AudioSegment.empty()
        for character in converted_text:
            if character == '.':
                output_sound_file += self.dit_sound
            elif character == '-':
                output_sound_file += self.duh_sound
            elif character == ' ':
                output_sound_file += self.intra_space_sound
            elif character == '/':
                output_sound_file += self.intra_space_sound * 7
        play(output_sound_file)
