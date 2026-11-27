import pytest
from ejercicio_2_unit_testing import count_characters, string_to_list, prime_number , prime_list

#----------------------------------------------------------------------
#------------------------- First Function Tests------------------------
#----------------------------------------------------------------------

# Test 1: Count uppercase and lowercase characters
def test_count_characters_uppercase_and_lowercase_characters():

    # Arrange
    word = "I love Nación Sushi"
    expected = (3, 13)

    # Act
    result = count_characters(word)

    # Assert
    assert result == expected


# Test 2: Empty string
def test_count_characters_empty_string():

    # Arrange
    word = ""
    expected = (0, 0)

    # Act
    result = count_characters(word)

    # Assert
    assert result == expected


# Test 3: Uppercase characters only
def test_count_characters_uppercase_only():

    # Arrange
    word = "HELLO WORLD"
    expected = (10, 0)

    # Act
    result = count_characters(word)

    # Assert
    assert result == expected


# Test 4: Lowercase characters only
def test_count_characters_lowercase_only():

    # Arrange
    word = "hello world"
    expected = (0, 10)

    # Act
    result = count_characters(word)

    # Assert
    assert result == expected


# Test 5: Numbers and special characters
def test_count_characters_special_characters():

    # Arrange
    word = "Hello World 123!"
    expected = (2, 8)

    # Act
    result = count_characters(word)

    # Assert
    assert result == expected

#----------------------------------------------------------------------
#------------------------- Second Function Tests------------------------
#----------------------------------------------------------------------

# Test 6: Sort words alphabetically
def test_string_to_list():

    # Arrange
    text = "python-variable-funcion-computadora-monitor"
    expected = "computadora-funcion-monitor-python-variable"

    # Act
    result = string_to_list(text)

    # Assert
    assert result == expected


# Test 7: Single word
def test_string_to_list_single_word():

    # Arrange
    text = "python"
    expected = "python"

    # Act
    result = string_to_list(text)

    # Assert
    assert result == expected


# Test 8: Empty string
def test_string_to_list_empty_string():

    # Arrange
    text = ""
    expected = ""

    # Act
    result = string_to_list(text)

    # Assert
    assert result == expected


#----------------------------------------------------------------------
#------------------------- Third Function Tests------------------------
#----------------------------------------------------------------------

# Test 9: Prime number
def test_prime_number():

    # Arrange
    number = 7
    expected = True

    # Act
    result = prime_number(number)

    # Assert
    assert result == expected


# Test 10: Composite number
def test_prime_number_composite():

    # Arrange
    number = 9
    expected = False

    # Act
    result = prime_number(number)

    # Assert
    assert result == expected


# Test 11: Number one is not prime
def test_prime_number_one():

    # Arrange
    number = 1
    expected = False

    # Act
    result = prime_number(number)

    # Assert
    assert result == expected


# Test 12: Number two is prime
def test_prime_number_two():

    # Arrange
    number = 2
    expected = True

    # Act
    result = prime_number(number)

    # Assert
    assert result == expected


# Test 13: Negative number
def test_prime_number_negative():

    # Arrange
    number = -5
    expected = False

    # Act
    result = prime_number(number)

    # Assert
    assert result == expected


# Test 14: Zero is not prime
def test_prime_number_zero():

    # Arrange
    number = 0
    expected = False

    # Act
    result = prime_number(number)

    # Assert
    assert result == expected


# Test 15: List with prime and composite numbers
def test_prime_list():

    # Arrange
    numbers = [1, 4, 6, 7, 13, 9, 67]
    expected = [7, 13, 67]

    # Act
    result = prime_list(numbers)

    # Assert
    assert result == expected


# Test 16: Empty list
def test_prime_list_empty():

    # Arrange
    numbers = []
    expected = []

    # Act
    result = prime_list(numbers)

    # Assert
    assert result == expected


# Test 17: List without prime numbers
def test_prime_list_without_primes():

    # Arrange
    numbers = [1, 4, 6, 8, 9, 10]
    expected = []

    # Act
    result = prime_list(numbers)

    # Assert
    assert result == expected


# Test 18: List with only prime numbers
def test_prime_list_only_primes():

    # Arrange
    numbers = [2, 3, 5, 7, 11]
    expected = [2, 3, 5, 7, 11]

    # Act
    result = prime_list(numbers)

    # Assert
    assert result == expected