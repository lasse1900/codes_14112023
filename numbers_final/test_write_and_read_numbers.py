# test_write_and_read.py
# Windows / MacOs, please run script with command: [pytest -v -s test_write_and_read_numbers.py]
# Ubuntu (22.04.3 LTS) please run script with command: [python3 -m pytest -v -s test_write_and_read_numbers.py]
# With decorators command e.g. [pytest -s -v -m smoke] or [pytest -s -v -m half]

import pytest
from write_and_read_numbers import write_numbers_to_file, read_and_print_all_numbers, read_and_print_half_from_file

@pytest.fixture
def numbers_file(tmpdir):
    filename = tmpdir.join("numbers.txt")
    write_numbers_to_file(filename)
    return filename

@pytest.mark.smoke
def test_read_and_print_all_numbers(capsys, numbers_file):
    read_and_print_all_numbers(numbers_file)
    captured = capsys.readouterr()

    expected_output = "Numbers 1 to 100: " + ' '.join(map(str, range(1, 101))) + '\n'
    print(expected_output)
    assert captured.out == expected_output

@pytest.mark.smoke
@pytest.mark.half
def test_read_and_print_half_from_file(capsys, numbers_file):
    read_and_print_half_from_file(numbers_file)
    captured = capsys.readouterr()

    expected_output = "Numbers 1 to 50: " + ' '.join(map(str, range(1, 51))) + '\n'
    print(expected_output)
    assert captured.out == expected_output