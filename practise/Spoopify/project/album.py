# from Spoopify.project.song import Song
# from typing import List


class Album:
    # songs: List[Song]

    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song_names = [s.name for s in self.songs]
        if song_name not in song_names:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        self.songs.pop(song_names.index(song_name))
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        res = [f"Album {self.name}\n"] + [f"== {s.get_info()}\n" for s in self.songs]
        return "".join(res)

