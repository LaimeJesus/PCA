import unittest

from hypergraph import _cartesian, _dimensions, _tuplesToList, buildHypergraphComplement


class TestHypergraph(unittest.TestCase):
    '''
    @TODO move this file into their own test folder
    '''
    def test_dimensionsEmpty(self):
        self.assertEqual(_tuplesToList(_dimensions([])), [])

    def test_dimensionsOfTwoColumns(self):
        list_dimensions = _tuplesToList(_dimensions([1, 2]))
        expected = [[0], [0, 1]]
        self.assertEqual(list_dimensions, expected)

    def test_cartesianEmpty(self):
        self.assertEqual(_cartesian([]), [[]])

    def test_cartesianProduct(self):
        product = _cartesian([[0, 1], [2, 3]])
        expected = [[0, 2], [0, 3], [1, 2], [1, 3]]
        self.assertEqual(product, expected)

    def test_buildHypergraphEmpty(self):
        context = [[], 0]
        hg = buildHypergraphComplement(context)
        self.assertEqual(hg, [])

    def test_buildHypergraphWithContext(self):
        context = [[[0, 1], [1, 2], [2, 3]], 3, 3]
        hg = buildHypergraphComplement(context)
        expected = [[0, 3], [0, 5], [1, 3], [1, 4], [2, 3], [2, 4], [2, 5]]
        self.assertEqual(hg, expected)


if __name__ == '__main__':
    unittest.main()
