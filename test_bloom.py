from bloom import BloomFilter


def test_bloom_py():
    bf = BloomFilter(10, 0.01)
    bf.insert("1")
    bf.insert("2")
    bf.insert("42")

    assert bf.lookup("1")
    assert bf.lookup("2")
    assert bf.lookup("42")
    assert not bf.lookup("99")
