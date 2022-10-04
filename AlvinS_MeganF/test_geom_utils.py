import geom_utils as gu

def test_is_point_in_box_LeftOfBox():
    expected = False
    actual = gu.is_point_in_box()
    assert expected == actual

def test_is_point_in_box_OnLeftEdge():
    expected = False
    actual = gu.is_point_in_box()
    assert expected == actual

def test_is_point_in_box_AboveBox():
    expected = False
    actual = gu.is_point_in_box()
    assert expected == actual

def test_is_point_in_box_OnTopEdge():
    expected = False
    actual = gu.is_point_in_box()
    assert expected == actual

def test_is_point_in_box_RightOfBox():
    expected = False
    actual = gu.is_point_in_box()
    assert expected == actual

def test_is_point_in_box_OnRightEdge():
    expected = False
    actual = gu.is_point_in_box()
    assert expected == actual

def test_is_point_in_box_BelowBox():
    expected = False
    actual = gu.is_point_in_box()
    assert expected == actual

def test_is_point_in_box_OnBottomEdge():
    expected = False
    actual = gu.is_point_in_box()
    assert expected == actual

def test_is_point_in_box_InBox():
    expected = True
    actual = gu.is_point_in_box()
    assert expected == actual






