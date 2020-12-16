def get_lines(filename: str) -> list:
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines