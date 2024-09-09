"""Test file containing test case for merge sort"""
from hw2_debugging import merge_sort


def test_merge_sort():
    """Four test cases to test the correct merge sort function"""
    assert merge_sort(
        [23, 45, 10, 67, 34, 89, 1, 78, 21, 55]
    ) == [1, 10, 21, 23, 34, 45, 55, 67, 78, 89]

    assert merge_sort(
        [97, 85, 70, 63, 41, 30, 28, 14, 11, 3]
    ) == [3, 11, 14, 28, 30, 41, 63, 70, 85, 97]

    assert merge_sort([7]) == [7]
    assert merge_sort([]) == []
