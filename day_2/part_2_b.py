from intcode.intcode import Intcode

def read_program():
    with open("day_2/input.txt") as f:
        line = f.readline()
        return [int(x) for x in line.split(",")]

def get_result(a, b, machine):
    machine.reset()
    machine.program[1] = a
    machine.program[2] = b
    machine.run()
    return machine.program[0]

if __name__ == "__main__":
    program = read_program()
    machine = Intcode(program)

    target = 19690720
    for a in range(100):
        for b in range(100):
            result = get_result(a, b, machine)
            if result == target:
                print(f"a, b of {a, b} gives our target score")
                print(f"answer is {100*a + b}")
