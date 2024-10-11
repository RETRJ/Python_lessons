import task_casts


def test_a_new():
    assert hasattr(task_casts, 'a_new'), 'The variable a_new is not defined.'
    assert isinstance(task_casts.a_new, float), 'a_new should be a float.'


def test_b_new():
    assert hasattr(task_casts, 'b_new'), 'The variable b_new is not defined.'
    assert isinstance(task_casts.b_new, int), 'b_new should be an int.'


def test_c_new():
    assert hasattr(task_casts, 'c_new'), 'The variable c_new is not defined.'
    assert isinstance(task_casts.c_new, int), 'c_new should be an int.'


def test_d_new():
    assert hasattr(task_casts, 'd_new'), 'The variable d_new is not defined'
    assert isinstance(task_casts.d_new, str), 'd_new should be a string.'


def test_e_new():
    assert hasattr(task_casts, 'e_new'), 'The variable e_new is not defined.'
    assert isinstance(task_casts.e_new, bool), 'e_new should be a boolean.'
