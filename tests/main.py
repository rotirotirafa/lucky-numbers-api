from src.core import generator, check_six_size


def test_generator_is_int():
    quantity = 60
    result = generator(quantity)
    assert type(result) is int


def test_generator_is_inside_range():
    quantity = 60
    result = generator(quantity)
    assert result <= quantity


def test_true_length_from_numbers():
    quantity = [1, 10, 3, 10, 18]
    result = check_six_size(quantity)
    assert result is True


def test_false_length_from_numbers():
    quantity = [1, 10, 3, 10, 18, 14, 9]
    result = check_six_size(quantity)
    assert result is False
