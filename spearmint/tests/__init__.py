import pytest

def assert_raises(e, fx, *args):
    if issubclass(e, Exception):
        with pytest.raises(e):
            fx(*args)
    elif issubclass(e, Warning):
        with pytest.warns(e):
            fx(*args)
    else:
        print(e.__class__)
        raise NotImplementedError()