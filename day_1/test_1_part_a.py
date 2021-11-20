import pytest

from day_1.part_1_a import calc_fuel_for_mass


@pytest.mark.parametrize(
    "mass, fuel", [[12, 2], [14, 2], [1969, 654], [100756, 33583], [3, 0]]
)
def test_calc_fuel_for_module(mass, fuel):
    assert calc_fuel_for_mass(mass) == fuel
