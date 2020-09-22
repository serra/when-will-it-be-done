import metrics


def test_always_true():
    assert metrics.always_true() == True


def test_always_false():
    assert metrics.always_true() == False
