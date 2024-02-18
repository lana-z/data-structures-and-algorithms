import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_hash():
    """
    intentionally breaks encapsulation by accessing internal attriubutes
    """
    hashtable = Hashtable()
    actual = hashtable._hash("Lana")
    assert 0 <= actual < hashtable._size


# @pytest.mark.skip("TODO")
def test_hash_twice():
    """
    intentionally breaks encapsulation by accessing internal attriubutes
    """
    hashtable = Hashtable()
    first = hashtable._hash("Lana")
    second = hashtable._hash("Lana")
    assert first == second


# @pytest.mark.skip("TODO")
def test_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "can make apple sauce")
    actual = hashtable.get("apple")
    expected = "can make apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_apple_again():
    hashtable = Hashtable()
    hashtable.set("apple", "can make apple sauce")
    hashtable.set("apple", "has a worm")
    actual = hashtable.get("apple")
    expected = "has a worm"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_key_not_exists():
    hashtable = Hashtable()
    actual = hashtable.get("key is not there")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_key_not_exists_again():
    """
    requires that act & cat hash the same
    """
    hashtable = Hashtable()
    hashtable.set("cat", "meow")
    actual = hashtable.get("act")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "can make apple sauce")
    hashtable.set("banana", "great in banana bread")
    actual = hashtable.keys()
    expected = ["apple", "banana"]
    assert sorted(actual) == sorted(expected)


# @pytest.mark.skip("TODO")
def test_has():
    hashtable = Hashtable()
    hashtable.set("apple", "can make apple sauce")
    hashtable.set("banana", "great in a banana bread")
    assert hashtable.has("apple")
    assert hashtable.has("banana")
    assert not hashtable.has("cucumber")


# @pytest.mark.skip("TODO")
def test_keys_repeats():
    hashtable = Hashtable()
    hashtable.set("apple", "can make apple sauce")
    hashtable.set("apple", "has a worm")
    hashtable.set("banana", "great in a banana bread")
    actual = hashtable.keys()
    expected = ["apple", "banana"]
    assert sorted(actual) == sorted(expected)


@pytest.mark.skip("TODO")
def test_internals():
    """
    there's a test_internals in your DSA repo that isn't a great fit.
    Feel free to ignore it
    Or tweak it as a STRETCH
    """
    pass
