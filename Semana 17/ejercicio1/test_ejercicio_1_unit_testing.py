import pytest
from ejercicio_1_unit_testing import bubble_sort

# Test 1: Small list
def test_bubble_sort_small_list():

    # Arrange
    numbers = [5, 3, 8, 1, 2]
    expected = [1, 2, 3, 5, 8]

    # Act
    bubble_sort(numbers)

    # Assert
    assert numbers == expected


# Test 2: Large list (more than 100 elements)
def test_bubble_sort_large_list():

    # Arrange
    numbers = list(range(150, 0, -1))
    expected = list(range(1, 151))

    # Act
    bubble_sort(numbers)

    # Assert
    assert numbers == expected


# Test 3: Empty list
def test_bubble_sort_empty_list():

    # Arrange
    numbers = []

    # Act
    bubble_sort(numbers)

    # Assert
    assert numbers == []


# Test 4: Invalid parameters (string)
def test_bubble_sort_invalid_parameter_string():

    # Act & Assert
    with pytest.raises(TypeError):
        bubble_sort("Hello")

# Test 5: Invalid parameters (integer)
def test_bubble_sort_invalid_parameter_integer():

    # Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(123)

# Test 6: Invalid parameters (float)
def test_bubble_sort_invalid_parameter_float():

    # Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(5.5)

# Test 5: Invalid parameters (tuple)
def test_bubble_sort_invalid_parameter_tuple():

    # Act & Assert
    with pytest.raises(TypeError):
        bubble_sort((5,3,1))

# Test 5: Invalid parameters (None)
def test_bubble_sort_invalid_parameter_none():

    # Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(None)