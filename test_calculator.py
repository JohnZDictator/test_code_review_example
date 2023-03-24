import pytest

def addition(x, y):
    # Todo: add x & y
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("X & Y should be of type num")
    # return x + y
    
def subtraction(x, y):
    # Todo: subtract y from x
    pass
def multiplication(x, y):
    # Todo: multiply x & y
    pass
def division(x, y):
    # Todo: divide x by y
    pass

def test_addition():
    # arrange
    # act
    # assert
    with pytest.raises(TypeError):
        addition("2", 3)
    with pytest.raises(TypeError):
        addition(2, "3")
    with pytest.raises(TypeError):
        addition("2", "3")
    # with pytest.raises(TypeError):
    #     addition(None, 3)
    # with pytest.raises(TypeError):
    #     addition(2, None)
    # with pytest.raises(TypeError):
    #     addition(None, None)

    
# def test_subtraction():
#     # arrange
#     # act
#     # assert
#     pass
# def test_multiplication():
#     # arrange
#     # act
#     # assert
#     pass
# def test_division():
#     # arrange
#     # act
#     # assert
#     pass