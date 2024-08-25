from myFile import calculate_factorial

def test_calculate_factorial():
    assert(calculate_factorial(5)==120)
    assert(calculate_factorial(6)==720)

def test_calculate_factorial_negative():
    assert(calculate_factorial(-2)== "No real number solution exists for negative number")


