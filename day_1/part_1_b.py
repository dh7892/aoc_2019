from day_1.part_1_a import calc_fuel_for_mass, fuel_for_modules


def calc_total_fuel_for_module(module_mass):
    # Calculate fuel for module + parasitic mass
    total_mass = calc_fuel_for_mass(module_mass)

    additional_fuel = calc_fuel_for_mass(total_mass)
    while additional_fuel:
        total_mass += additional_fuel
        additional_fuel = calc_fuel_for_mass(additional_fuel)

    return total_mass


if __name__ == "__main__":
    # Get fuel for modules
    print(f"Total fuel is {fuel_for_modules(calc_total_fuel_for_module)}")
