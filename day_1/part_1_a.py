def calc_fuel_for_mass(mass):
    # Divide by 3
    answer = mass / 3

    # Round down
    answer = int(answer)

    # subtract 2
    answer -= 2

    if answer < 0:
        answer = 0

    return answer


def read_input():
    """
    Read the file input.txt into a list
    """
    with open("input.txt") as f:
        lines = f.readlines()

    return lines


def fuel_for_modules(fuel_func):
    """
    Read the input file and calculate the fuel for all the modules

    we pass the fuel calculation function as an argument for dependency injection
    """
    modules = [int(x) for x in read_input()]
    return sum([fuel_func(x) for x in modules])


if __name__ == "__main__":
    print(f"Total fuel is {fuel_for_modules(calc_fuel_for_mass)}")
