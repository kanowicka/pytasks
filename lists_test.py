import pytest #pylint:disable=unused-import
from lists import seq_sort

def test_seq_sort_ascending():
    assert seq_sort([6,5,4,99,3,2,1]) == [1,2,3,4,5,6,99]

def test_seq_sort_descending():
    assert seq_sort([6,5,4,99,3,2,1], True) == [99,6,5,4,3,2,1]

def test_seq_sort_empty():
    assert not seq_sort([]) == []

def test_seq_sort_duplicates():
    assert seq_sort([6,5,4,99,3,2,1,5,4,3,2,1]) == [1,1,2,2,3,3,4,4,5,5,6,99]
    assert seq_sort([6,5,4,99,3,2,1,5,4,3,2,1], True) == [99,6,5,5,4,4,3,3,2,2,1,1]
