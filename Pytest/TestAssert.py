def test_number():
    assert 5 == 5, "Not okay!"
    assert 3 == 5, "Not okay!"


def test_string():
    assert 'Hello' != 'Hi', "Its equal man!"
    assert 'Hi' != 'Hi', "Its equal man!"


def test_comparison():
    assert 5 < 9, 'Greater than it is!'
    assert 19 < 9, 'Greater than it is!'

def test_membership():
    l = [1, 2, 3]
    assert 1 in l, 'Not present'
    assert 5 in l, 'Not present'
