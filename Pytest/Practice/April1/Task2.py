"""
TASK 2: Pytest Markers Practice

Create 2 custom markers:
@pytest.mark.smoke
@pytest.mark.regression
Write:
2 test cases for smoke
2 test cases for regression
Each test should:
Contain a simple assertion
Run tests using:
Only smoke tests
Only regression tests
"""

import pytest


# Smoke
@pytest.mark.smoke
def test_number():
    assert 4 < 5, "Not less than"


@pytest.mark.smoke
def test_string():
    assert 'Hello' != 'Hi', "Equal"


# Regression
@pytest.mark.regression
def test_comparison():
    assert 9 == 9, 'Not Equal'


@pytest.mark.regression
def test_membership():
    l = ['a', 'b', 'c']
    assert 'd' not in l, 'It is present'
