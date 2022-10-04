import countdown as cd

def test_get_countdown_as_text_using_for():
    expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    actual = cd.get_countdown_as_text_using_for()
    assert expected == actual

def test_get_countdown_as_text_using_while():
    expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    actual = cd.get_countdown_as_text_using_while()
    assert expected == actual