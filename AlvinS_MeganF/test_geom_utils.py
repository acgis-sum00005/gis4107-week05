import geom_utils as gu

xmin = ymin = 1
xmax = ymax = 5

def test_is_point_in_box_LeftOfBox():
    expected = False
    actual = gu.is_point_in_box(.5, 5, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_OnLeftEdge():
    expected = False
    actual = gu.is_point_in_box(1, 5, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_AboveBox():
    expected = False
    actual = gu.is_point_in_box(1, 6, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_OnTopEdge():
    expected = False
    actual = gu.is_point_in_box(1, 5, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_RightOfBox():
    expected = False
    actual = gu.is_point_in_box(6, 5, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_OnRightEdge():
    expected = False
    actual = gu.is_point_in_box(5, 5, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_BelowBox():
    expected = False
    actual = gu.is_point_in_box(1, 0, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_OnBottomEdge():
    expected = False
    actual = gu.is_point_in_box(1, 1, xmin, ymin, xmax, ymax)
    assert expected == actual

def test_is_point_in_box_InBox():
    expected = True
    actual = gu.is_point_in_box(2, 3, xmin, ymin, xmax, ymax)
    assert expected == actual






