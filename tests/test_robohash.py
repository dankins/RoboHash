import unittest
from robohash import RoboHash


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_basics(self):
        h = RoboHash()
        h.insert(1, "foo")
        res = h.get(1)
        self.assertEqual(res, "foo")

    def test_resize(self):
        h = RoboHash(1117)
        for x in range(0, 120050):
            h.insert(x, x*2)

        for x in range(0, 120050):
            val = h.get(x)
            self.assertEquals(val, x*2)

        stats = h.get_stats()
        # resizes: 1117 -> 2235 -> 4471 -> 8943 -> 17887 -> 35775 -> 71551 -> 143103
        self.assertEqual(stats.resizes, 7)
        self.assertEqual(h.array_size, 143103)
        print("test_resize")
        h.stats.pretty_print()
        print("\n")

    def test_overwrite(self):
        h = RoboHash()
        h.insert(0, "old")
        self.assertEqual(h.get(0), "old")
        h.insert(0, "new")
        self.assertEqual(h.get(0), "new")

    def test_word_keys(self):
        h = RoboHash()
        print("test_word_keys")
        h.insert("foo", "foo2")
        h.insert("bar", "bar2")
        self.assertEqual(h.get("foo"), "foo2")
        self.assertEqual(h.get("bar"), "bar2")
        h.pretty_print()
        h.stats.pretty_print()
        print("\n")

if __name__ == '__main__':
    unittest.main()