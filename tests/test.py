from mypackage import myModule

def test_top_n():
    """
    perform test on top_n function
    """
    assert myModule.top_n([1, 7, 2, 3, 9, 20], 3) == [20, 9, 7], "incorrect" 
    assert myModule.top_n([2, 8, -1, 3, -2], 4) == [8, 3, 2, -1], "incorrect" 

