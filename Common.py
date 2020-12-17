def get_lines(filename: str) -> list:
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines


def get_int_lines(filename: str) -> list:
    lines = get_lines(filename)
    new_list = []
    for line in lines:
        new_list.append(int(line.strip()))
    return new_list