import pytest

def get_letter(string):
    if string == "A":
        return 1
    elif string == "B":
        return 2
    else:
        return 3
    

@pytest.mark.parametrize("input_string, expected_result", [
    ("A", 1),
    ("B", 2),
    ("C", 3),
])


def test_my_function(input_string, expected_result):
    # Assuming you have a function called my_function that processes the input_string
    result = get_letter(input_string)
    assert result == expected_result
