from Solution import compute_output

if __name__ == "__main__":

    assert compute_output([1,2,3,4,5]) == [120,60,40,30,24] , "Expected [120,60,40,30,24]"
    assert compute_output([3,2,1]) == [2,3,6], "Expected [2,3,6]"
    assert not compute_output([1,2,3,4,5]) == [2,3,6], "should be False"

    print("Everything passed")