from hw2_debugging import merge_sort


def test_correctly_sorted():

    assert merge_sort([1, 5, 4, 3, 2]) == [1, 2, 3, 4, 5]


def test_jumbled_order_or_correct_order():

    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_single_value():

    assert merge_sort([7]) == [7]
