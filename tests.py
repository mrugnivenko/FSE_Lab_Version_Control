from storage import Storage
import pytest

def test_add():
    st = Storage({})
    st.add('a', 5)
    key = 'a'
    val = st.get(key)
    assert val == 5, "Value for the key {} is not equal to expected".format(key)

def test_remove():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    st.remove(key)
    val = st.get(key)
    assert val is None, "Value for the key {} is not deleted".format(key)
    key = 'c'
    with pytest.raises(KeyError):
        st.remove(key)

def test_set():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    st.set(key, 3)
    assert st.get(key) == 3
    key = 'c'
    val = st.set(key, 4)
    assert val is None

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()