import unittest

from pca.concepts import fromHypergraphToConcepts


class TestConcepts(unittest.TestCase):

    def test_fromHypergraphToConceptsShouldNotBeEmpty(self):
        hypergraph = """"""
        self.assertRaises(ValueError, fromHypergraphToConcepts, hypergraph)

    def test_fromHypergraphToConceptsShouldContainMoreThanOneLine(self):
        hypergraph = """1 2 3"""
        self.assertRaises(ValueError, fromHypergraphToConcepts, hypergraph)

    def test_fromHypergraphToConceptsCreatesConcept(self):
        hypergraph = """3 5 4\n3 5 1 2\n0 3 4 2\n0 1 2\n4\n\n0\n0\n0\n2\n2"""
        concept = fromHypergraphToConcepts(hypergraph)
        expected = [['3', '5', '4'], ['3', '5', '1', '2'], ['0', '3', '4', '2'], ['0', '1', '2']]
        self.assertEqual(concept, expected)

    def test_fromTraversalToConcept(self):
        # @TODO NotImplemented
        pass

if __name__ == '__main__':
    unittest.main()
