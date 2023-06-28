import unittest

from pca.PCA import concepts


class TestPCA(unittest.TestCase):

    def test_conceptsWithEmptyContextRaiseException(self):
        self.assertRaises(Exception, concepts, [])

    def test_conceptsWithNonEmptyContext(self):
        context = [[[0, 1], [1, 2], [2, 3]], 3, 3]
        concepts_result = concepts(context)
        expected = [[{0, 1, 2}, set()], [{0}, {1}], [{1}, {2}], [set(), {0, 1, 2}]]
        self.assertEqual(concepts_result, expected)

if __name__ == '__main__':
    unittest.main()
