import pytest

from day_1.part_1_b import calc_total_fuel_for_module


@pytest.mark.parametrize(
    "mass, fuel",
    [
        [14, 2],
        [1969, 966],
        [100756, 50346],
    ],
)
def test_calc_fuel_for_module(mass, fuel):
    assert calc_total_fuel_for_module(mass) == fuel
