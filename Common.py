from timeit import timeit

def get_lines(filename: str) -> list:
    f = open(filename)
    lines = list(map(lambda line: line.rstrip(), f.readlines()))
    f.close()
    return lines


def get_int_lines(filename: str) -> list:
    lines = get_lines(filename)
    lines = list(map(int, lines))
    return lines

def time_function(func, iterations: int) -> int:
    sum_passwords_Toboggan = timeit(func, number=iterations)
    return sum_passwords_Toboggan/iterations
