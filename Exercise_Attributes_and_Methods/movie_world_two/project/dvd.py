import calendar


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int, is_rented: bool = False):
        self.name: str = name
        self.id: int = id
        self.creation_year: int = creation_year
        self.creation_month: str = creation_month
        self.age_restriction: int = age_restriction
        self.is_rented: bool = is_rented

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, creation_month, creation_year = map(int, date.split("."))
        creation_month = calendar.month_name[creation_month]
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {status}"

