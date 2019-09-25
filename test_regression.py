import LinearRegression as ln
def test_square_error():
    square_error = ln.squared_error(5,8)
    assert square_error!=0