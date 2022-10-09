import seqmod as sm

def test_mod_sequence_1(ABCD, None, None):
    expected = [ABCD]
    actual = sm.mod_sequence()
    assert expected == actual 

def test_mod_sequence_2(ABCD, 0, None):
    expected = [BCD]
    actual = sm.mod_sequence()
    assert expected == actual

def test_mod_sequence_3(ABCD, 1, None):
    expected = [ACD]
    actual = sm.mod_sequence()
    assert expected == actual

def test_mod_sequence_4(ABCD, 1, 2):
    expected = [A]
    actual = sm.mod_sequence()
    assert expected == actual

def test_mod_sequence_5(ABCD, 2, 2):
    expected = [AB]
    actual = sm.mod_sequence()
    assert expected == actual

def test_mod_sequence_6(ABCD, 3, 2):
    expected = [AB]
    actual = sm.mod_sequence()
    assert expected == actual

def test_mod_sequence_7(ABCD, 4, None):
    expected = [ABCD]
    actual = sm.mod_sequence()
    assert expected == actual

def test_mod_sequence_8(ABCD, None, 4):
    expected = [ABCD]
    actual = sm.mod_sequence()
    assert expected == actual

def test_mod_sequence_9(ABCD, 1, 4):
    expected = [ACD]
    actual = sm.mod_sequence()
    assert expected == actual
    
