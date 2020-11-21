import requests


class PassangersReader:
    def __init__(self):
        self.results_per_page = 5
        self.current_page = 0
        response = requests.get("https://api.instantwebtools.net/v1/passenger?page=0&size=5")
        data = response.json()  # parsing to python
        self.index_in_current_page = 0
        self.total_pages: int = data["totalPages"]
        self.results_on_page: list = data["data"]

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index_in_current_page
        if self.index_in_current_page < self.results_per_page:
            self.index_in_current_page += 1
            return self.results_on_page[index]
        elif self.index_in_current_page >= self.results_per_page:
            self.current_page += 1
            response = requests.get(f"https://api.instantwebtools.net/v1/passenger?page={self.current_page}&size=5")
            self.results_on_page = response.json()["data"]
            self.index_in_current_page = 1
            return self.results_on_page[0]


passanger_reader = PassangersReader()

for passenger in passanger_reader:
    print(passenger)


