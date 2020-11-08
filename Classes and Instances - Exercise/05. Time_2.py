import datetime


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    hours: int
    minutes: int
    seconds: int

    def __init__(self, hh: int, mm: int, ss: int):
        self.hours = hh
        self.minutes = mm
        self.seconds = ss

    def set_time(self, hh: int, mm: int, ss: int) -> None:
        self.hours = hh
        self.minutes = mm
        self.seconds = ss

    def get_time(self) -> str:
        hours = f"{self.hours}".zfill(2)
        minutes = f"{self.minutes}".zfill(2)
        seconds = f"{self.seconds}".zfill(2)

        current_time = f"{hours}:{minutes}:{seconds}"

        return current_time

    def next_second(self) -> get_time:

        current_time = datetime.datetime(hour=self.hours, minute=self.minutes, second=self.seconds, year=1, month=1, day=1) + datetime.timedelta(seconds=1)

        self.hours = current_time.hour
        self.minutes = current_time.minute
        self.seconds = current_time.second

        return self.get_time()
