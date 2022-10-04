import fc_manager as fc

def test_get_feature_type_point():
    expected = "POINT"
    actual = fc.get_feature_type(1)
    assert expected == actual

def test_get_feature_type_polyline():
    expected = "POLYLINE"
    actual = fc.get_feature_type(2)
    assert expected == actual

def test_get_feature_type_polygon():
    expected = "POLYGON"
    actual = fc.get_feature_type(3)
    assert expected == actual

def test_get_feature_type_none():
    expected = "None"
    actual = fc.get_feature_type()
    assert expected == actual

