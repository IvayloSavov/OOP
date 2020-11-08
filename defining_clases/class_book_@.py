from dataclasses import dataclass


@dataclass()
class Book:
    name: str
    author: str
    pages: int

# Creating class without def __init__
# Arguments by default are after the positional arguments
