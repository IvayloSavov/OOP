# from Spoopify.project.album import Album
# from Spoopify.project.song import Song
# from typing import List


class Band:
    # albums = List[Album]

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_names = [a.name for a in self.albums]
        if album_name not in album_names:
            return f"Album {album_name} is not found."
        album = self.albums[album_names.index(album_name)]
        if album.published:
            return f"Album has been published. It cannot be removed."
        self.albums.remove(album)
        return f"Album {album.name} has been removed."

    def details(self):
        res = f"Band {self.name}\n" + "".join([f"{a.details()}" for a in self.albums])
        return res

#
# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
