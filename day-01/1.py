def fuel_required(mass):
    fuel = mass//3 - 2
    return max(fuel, 0)


def recursive_full_required(mass):
    fuel = 0
    while mass > 0:
        new_fuel = fuel_required(mass)
        fuel += new_fuel
        mass = new_fuel
    return fuel


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        masses = [int(x) for x in f.readlines()]
    # Part 1
    print(sum([fuel_required(x) for x in masses]))
    # Part 2
    print(sum(recursive_full_required(x) for x in masses))
