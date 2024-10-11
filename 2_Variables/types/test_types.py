from types import NoneType

import task_types


def test_a_int():
    assert hasattr(task_types, 'a'), "The variable 'a' is not defined"
    assert isinstance(task_types.a, int), "The variable 'a' is not of type int"


def test_b_float():
    assert hasattr(task_types, 'b'), "The variable 'b' is not defined"
    assert isinstance(task_types.b, float), "The variable 'b' is not of type float"


def test_c_str():
    assert hasattr(task_types, 'c'), "The variable 'c' is not defined"
    assert isinstance(task_types.c, str),  "The variable 'c' is not of type str"


def test_d_bool():
    assert hasattr(task_types, 'd'), "The variable 'd' is not defined"
    assert isinstance(task_types.d, bool), "The variable 'd' is not of type bool"


def test_e_none():
    assert hasattr(task_types, 'e'), "The variable 'e' is not defined"
    assert isinstance(task_types.e, NoneType), "The variable 'e' is not of type NoneType"
