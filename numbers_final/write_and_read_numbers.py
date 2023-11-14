# write_and_read_numbers.py

def write_numbers_to_file(filename):
    with open(filename, 'w') as file:
        for i in range(1, 101):
            file.write(str(i) + ' ')

def read_and_print_all_numbers(filename):
    with open(filename, 'r') as file:
        numbers = file.read().split()

    print("Numbers 1 to 100:", ' '.join(map(str, numbers)))


def read_and_print_half_from_file(filename):
    with open(filename, 'r') as file:
        numbers = file.read().split()

    half_length = int(len(numbers)/2)
    half_numbers = numbers[:half_length]

    print("Numbers 1 to 50:", ' '.join(map(str, half_numbers)))