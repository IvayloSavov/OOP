a = []


def main():
    try:
        if True:
            raise Exception("are you crazy")
        else:
            print(succes)
    except Exception as text:
        return repr(text)

print(main())


