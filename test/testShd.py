import unittest

from src.shd import shd_path, fromEdgesFileToHypergraph
from src.hypergraph import buildHypergraphEdges, writeHypergraphInFile

class TestShd(unittest.TestCase):

    def test_shdPathShouldContainsScriptsFolder(self):
        SHD_PATH = "scripts/shd"
        self.assertRegex(shd_path(), SHD_PATH)

    def test_shdFromEdgesFileToHypergraphShouldCreateAnHypergraphFromAFile(self):
        hypergraph_path="hypergraph.io"
        context = [[[0, 1], [1, 2], [2, 3]], 3, 3]
        HYPERGRAPH = buildHypergraphEdges(context)
        writeHypergraphInFile(HYPERGRAPH, hypergraph_path)
        result = fromEdgesFileToHypergraph(hypergraph_path)
        expected = "3 5 4\n3 5 1 2\n0 3 4 2\n0 1 2\n4\n0\n0\n0\n2\n2\n"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
