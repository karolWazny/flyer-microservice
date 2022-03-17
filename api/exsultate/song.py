import re

class SongPart:
    def __init__(self, content, type='verse'):
        self.content = content
        self.type = type

    @staticmethod
    def from_dict(dictionary):
        return SongPart(content=dictionary['content'], type=dictionary['type'])

    def lyrics(self):
        pattern = r'\[[^\]]*\]'
        return re.sub(pattern, '', self.content)

class Song:
    def __init__(self, title):
        self.title = title
        self.lyrics_author = None
        self.music_author = None
        self.translation_author = None
        self.content = []

    def add_song_part(self, songpart):
        self.content.append(songpart)

    @staticmethod
    def from_dict(dictionary):
        output = Song(dictionary['title'])
        output.lyrics_author = dictionary['lyrics']
        output.music_author = dictionary['music']
        # output.translation_author = dictionary['translated']
        content = dictionary['content']
        for song_part in content:
            output.add_song_part(SongPart.from_dict(song_part))
        return output

class SongBook:
    def __init__(self):
        self.songs = []

    def sort_songs(self):
        self.songs.sort(key=SongBook.compare_function)

    @staticmethod
    def compare_function(e):
        return e.title

    @staticmethod
    def from_dict(dictionary):
        output = SongBook()
        song_dicts = dictionary
        for dict in song_dicts:
            output.songs.append(Song.from_dict(dict))
        output.sort_songs()
        return output