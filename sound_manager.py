from pathlib import Path
from pydub import AudioSegment
from pydub.playback import play


class SoundCreator:
    def __init__(self):
        self.duh_sound = AudioSegment.from_file(self.get_sound_file_path('dit.mp3'), format='mp3')
        self.dit_sound = AudioSegment.from_file(self.get_sound_file_path('duh.mp3'), format='mp3')
        self.intra_space_sound = AudioSegment.from_file(self.get_sound_file_path('intra_space.mp3'), format='mp3')

    def get_sound_file_path(self, sound_file):
        current_directory = Path.cwd()
        sound_file_path = current_directory / 'sounds' / sound_file
        return sound_file_path

    def player(self, converted_text):
        for character in converted_text:
            if character == '.':
                play(self.dit_sound)
            elif character == '-':
                play(self.duh_sound)
            elif character == ' ':
                play(self.intra_space_sound * 7)
