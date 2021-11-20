"""
The intcode machine
"""

import copy
from enum import Enum


class Status(Enum):
    OK = 1
    ERROR = 2
    END = 3


class Intcode:
    def __init__(self, program):
        self.initial_program = copy.deepcopy(program)
        self.operations = {1: self.add, 2: self.multiply, 99: self.exit}
        self.reset()

    def reset(self):
        self.program = copy.deepcopy(self.initial_program)
        self.position = 0
        self.status = Status.OK
        self.input = 0
        self.output = 0

    def run(self, input=0):
        """
        Run the whole program
        """
        self.input = input
        while self.status == Status.OK:
            self.execute_command()

    def save_input(self):
        """
        Take the value from our input buffer and save it in the program at
        the address secified in out parameter
        """
        self.program[self.program[self.position]] = self.input
        self.position += 1

    def save_output(self):
        """
        Take the value from the appropriate location in the code and save it to
        our output buffer
        """
        self.output = self.program[self.program[self.position]]
        self.position += 1

    def execute_command(self):
        """
        Run the next command
        """
        opcode = self.get_value()
        try:
            command = self.operations[opcode]
        except KeyError:
            self.status = Status.ERROR

        if self.status == Status.OK:
            command()

    def get_value(self):
        """
        Return the value at the current location and advance
        """
        value = self.program[self.position]
        self.position += 1
        return value

    def get_from_location(self):
        """
        Return the number stored in the address that's stored in our
        current position.

        We also advance the position

        I.e. The number at our current position tells us the address to look up
        (we're not talking about just getting the number at the current position)
        """
        value = self.program[self.program[self.position]]
        self.position += 1
        return value

    def set_at_location(self, value):
        """
        Put the supplied value in the memory address pointed to by the value
        under our current position and advance by one
        """
        self.program[self.program[self.position]] = value
        self.position += 1

    def add(self):
        lhs = self.get_from_location()
        rhs = self.get_from_location()
        self.set_at_location(lhs + rhs)

    def multiply(self):
        lhs = self.get_from_location()
        rhs = self.get_from_location()
        self.set_at_location(lhs * rhs)

    def exit(self):
        self.status = Status.END
