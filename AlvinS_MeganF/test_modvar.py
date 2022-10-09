import modvar as mod

def test_mod_myvar_condition1():
    expected = 9
    actual = mod.mod_myvar(1)
    assert expected == actual

def test_mod_myvar_condition2():
    expected = 2
    actual = mod.mod_myvar(3)
    assert expected == actual

def test_mod_myvar_condition3():
    expected = 4
    actual = mod.mod_myvar(2)
    assert expected == actual

def test_mod_myvar_condition4():
    expected = 10
    actual = mod.mod_myvar(12)
    assert expected == actual