import LinearRegression as ln
import numpy as np
def test_square_error():
    origs = [5,6,7]
    line = [6,7,10]
    square_error = ln.squared_error(np.array(origs, dtype=np.float64),np.array(line, dtype=np.float64))
    assert square_error!=0