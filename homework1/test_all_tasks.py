import task1
import task2
import task3
import task4
import task5
import task6
import task7
import pytest
import numpy as np
import os

# Task 1 Tests
def test_hello_world(capsys):
    task1.print_hello_world()

    # Get output from console
    console = capsys.readouterr()
    assert console.out == "Hello, World!\n"

# Task 2 Tests
def test_int():
    assert isinstance(task2.return_int(), int)

def test_float():
    assert isinstance(task2.return_float(), float)

def test_string():
    assert isinstance(task2.return_string(), str)

def test_bool():
    assert isinstance(task2.return_bool(), bool)


# Task 3 Tests
def test_num():
    assert task3.check_num(1) == "Positive"

    assert task3.check_num(-1) == "Negative"

    assert task3.check_num(0) == "Zero"

def test_find_primes():
    assert task3.find_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum():
    assert task3.sum_ints(100) == 5050


# Task 4 Tests
def test_calculate_discount():
    # Test with integers
    assert task4.calculate_discount(100, 20) == 80
    assert task4.calculate_discount(200, 50) == 100
    
    # Test with floats
    assert task4.calculate_discount(100.0, 20.0) == 80.0
    assert task4.calculate_discount(48.3, 12.5) == pytest.approx(42.26, rel=1e-2)

# Task 5 Tests
def test_favorite_books_list():
    # Checks that it is a list and in the list it is a tuple (book, author)
    assert isinstance(task5.favorite_books_list, list)
    assert all(isinstance(book, tuple) and len(book) == 2 for book in task5.favorite_books_list)

def test_first_three_books():
    # Checks if list was sliced correctly
    expected_books = task5.favorite_books_list[:3]
    assert task5.first_three_books == expected_books  

def test_student_database():
    """Test if the student database is a valid dictionary with correct mappings."""
    assert isinstance(task5.student_database_dict, dict)  # Ensure it's a dictionary
    assert len(task5.student_database_dict) >= 3  # Ensure at least 3 students exist
    assert all(isinstance(k, str) and isinstance(v, str) for k, v in task5.student_database_dict.items())  # Ensure correct key-value types

# Task6 Tests - Had help from ChatGPT
expected_word_counts = {
    "task6_read_me.txt": 104  
}


def _make_test_func(filename):
    """Generates a test function for a given filename."""
    def test_func():
        expected_count = expected_word_counts.get(filename, 0)
        result = task6.count_words_in_file(filename)
        assert (
            result == expected_count
        ), f"Expected {expected_count} got {result}."
    return test_func

# Create test functions at runtime
for txt_file in expected_word_counts:
    # Create a function name based on the text file name
    test_name = f"test_count_words_in_{txt_file.replace('.', '_')}"

    globals()[test_name] = _make_test_func(txt_file)

# Task 7 Tests
def test_numpy_sum():
    assert task7.sum_numpy_array(np.array([1,2,3])) == 6
    assert task7.sum_numpy_array(np.array([])) == 0
    
