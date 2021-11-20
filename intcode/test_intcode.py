import pytest

from intcode import Intcode, Status


@pytest.fixture
def program_1():
    code = [1, 0, 0, 4, 10]
    machine = Intcode(code)
    return machine


@pytest.fixture
def program_2():
    code = [2, 0, 0, 4, 10]
    machine = Intcode(code)
    return machine


@pytest.fixture
def program_3():
    code = [2, 0, 0, 0, 99]
    machine = Intcode(code)
    return machine


def test_addition(program_1):
    program_1.execute_command()
    assert program_1.program == [1, 0, 0, 4, 2]


def test_multiplication(program_2):
    program_2.execute_command()
    assert program_2.program == [2, 0, 0, 4, 4]


def test_reset(program_1):
    program_1.execute_command()
    assert program_1.program == [1, 0, 0, 4, 2]
    program_1.reset()
    assert program_1.program == [1, 0, 0, 4, 10]
    assert program_1.position == 0


@pytest.mark.parametrize(
    "program, end_status, end_program",
    [
        [[1, 0, 0, 0, 99], Status.END, [2, 0, 0, 0, 99]],
        [[666, 0, 0, 0, 99], Status.ERROR, [666, 0, 0, 0, 99]],
    ],
)
def test_run(program, end_status, end_program):
    machine = Intcode(program)
    machine.run()
    assert machine.status == end_status
    assert machine.program == end_program
