"""Test file containing test case for merge sort"""
from hw2_debugging import merge_sort


def test_merge_sort_normal_case():
    """Test merge sort with a standard list of integers"""
    assert merge_sort(
        [23, 45, 10, 67, 34, 89, 1, 78, 21, 55]
    ) == [1, 10, 21, 23, 34, 45, 55, 67, 78, 89]


def test_merge_sort_reverse_order():
    """Test merge sort with a reverse-ordered list"""
    assert merge_sort(
        [97, 85, 70, 63, 41, 30, 28, 14, 11, 3]
    ) == [3, 11, 14, 28, 30, 41, 63, 70, 85, 97]


def test_merge_sort_single_element():
    """Test merge sort with a single-element list"""
    assert merge_sort([7]) == [7]


def test_merge_sort_empty_list():
    """Test merge sort with an empty list"""
    assert merge_sort([]) == []
