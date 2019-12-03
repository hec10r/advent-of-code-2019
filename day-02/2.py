def restore_gravity(intcode_, noun, verb):
    intcode = [_ for _ in intcode_]
    intcode[1] = noun
    intcode[2] = verb
    size = len(intcode_) // 4
    for i in range(size):
        j = 4 * i
        if intcode[j] == 99:
            break
        elif intcode[j] == 1:
            intcode[intcode[j + 3]] = intcode[intcode[j + 1]] + intcode[intcode[j + 2]]
        elif intcode[j] == 2:
            intcode[intcode[j + 3]] = intcode[intcode[j + 1]] * intcode[intcode[j + 2]]
    return intcode[0]


def find_noun_verb(intcode_, desired_output):
    for noun in range(100):
        for verb in range(100):
            if restore_gravity(intcode_, noun, verb) == desired_output:
                return 100 * noun + verb


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    original = [int(x) for x in data.split(',')]
    # Part 1
    print(restore_gravity(original, 12, 2))
    # Part 2
    print(find_noun_verb(original, 19690720))
