import unittest
from robohash import RoboHash


class TestSequenceFunctions(unittest.TestCase):

    def test_basics(self):
        h = RoboHash()
        h.insert(1, "foo")
        res = h.get(1)
        self.assertEqual(res, "foo")

    def test_resize(self):
        h = RoboHash(1117)
        for x in range(0, 120050):
            h.insert(x*999999, x*2)

        for x in range(0, 120050):
            val = h.get(x*999999)
            self.assertEquals(val, x*2)

        stats = h.get_stats()
        # resizes: 1117 -> 2235 -> 4471 -> 8943 -> 17887 -> 35775 -> 71551 -> 143103
        self.assertEqual(stats.resizes, 7)
        self.assertEqual(h.array_size, 143103)
        print("test_resize")
        h.stats.pretty_print()
        h.stats.print_distribution(h.storage, 10)
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

    def test_linear_probe_rollover(self):
        h = RoboHash(10)
        i = 0
        # find an int that hashes to the last bucket in the storage array
        while h.get_hash(i) != 9:
            i += 1

        h.insert(i, "first")

        # find another one that hashes to the same bucket
        j = i + 1
        while h.get_hash(j) != 9:
            j += 1

        h.insert(j, "second")

        self.assertEqual(h.get(i), "first")
        self.assertEqual(h.get(j), "second")
        print("test_linear_probe_rollover")
        h.pretty_print()
        print("\n")


if __name__ == '__main__':
    unittest.main()