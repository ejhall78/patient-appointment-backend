from ...utils import postcode

def test_valid_postcode():
    valid = "NN1 1AA"
    assert postcode.valid_postcode(valid)

    invalid = "aa"
    assert postcode.valid_postcode(invalid) == False

def test_format_valid_postcode():
    # Already formatted
    happy = "NN1 1AA"
    res = postcode.format_valid_postcode(happy)
    assert res == happy

    no_space = "NN11AA"
    res = postcode.format_valid_postcode(no_space)
    assert res == happy