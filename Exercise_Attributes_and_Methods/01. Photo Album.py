class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str) -> str:
        for index, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {page.index(label) + 1}"
        return "No more free spots"

    def display(self) -> str:
        res = f"{'-' * 11}\n"
        for pages in self.photos:
            res_2 = [f"[]" for _ in range(len(pages))]
            res += f"{' '.join(res_2)}\n{'-' * 11}\n"
        return res


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

