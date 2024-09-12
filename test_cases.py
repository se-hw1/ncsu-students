from hw2_debugging import merge_sort


def test_correctly_sorted():
    arr = [1, 5, 4, 3, 2]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]


def test_jumbled_order_or_correct_order():
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]


def check_sorting_negative_numbers():
    arr = [-5, -6, -1, -2, -3, -4]
    assert merge_sort(arr) == [-6, -5, -4, -3, -2, -1]
