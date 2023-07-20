import pytest

@pytest.mark.parametrize("input,expected",[
    ("a", "a"),
    ("b", "b"),
    ("c", "d")
])
def test_basic(input, expected):
    assert(input == expected)
    
    
@pytest.mark.skip(reason = "How to skip")
def test_skip():
    assert(1 == 1)
    
@pytest.mark.xfail #xpected fail
def test_dont_fail():
    assert(1 == 2)