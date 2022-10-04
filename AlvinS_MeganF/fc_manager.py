def get_feature_type(feature_code):
    if feature_code == 1:
        print("POINT")
    if feature_code == 2:
        print("POLYLINE")
    if feature_code == 3:
        print("POLYGON")
    else:
        print("NONE")

