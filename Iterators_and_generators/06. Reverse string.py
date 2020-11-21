def reverse_text(string):
    # for ch in string[::-1]:
    #     yield ch

    i = len(string)
    while i > 0:
        i -= 1
        yield string[i]


for char in reverse_text("step"):
    print(char, end='')

# reverse_text = lambda string: (ch for ch in reversed(string))