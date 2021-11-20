from intcode.intcode import Intcode

def read_program():
    with open("day_2/input.txt") as f:
        line = f.readline()
        return [int(x) for x in line.split(",")]

if __name__ == "__main__":
    program = read_program()
    machine = Intcode(program)

    # Change program to "Error State"
    machine.program[1] = 12
    machine.program[2] = 2
    machine.run()

    print(f"Final value at 0 is {machine.program[0]}")
