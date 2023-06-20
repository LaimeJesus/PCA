from itertools import product
from typing import Any, List, Tuple

Context = Tuple[List[List[int]], int, int]


def _dimensions(column_sizes: Any | List[int]) -> List[List[int]]:
    '''
    Given a list of numbers of size k, each number d_i represents a dimension
    Returns a list containing k lists and each sublist k_i with values from 0 to dimension d_i-1
    Example: _dimensions([1, 2, 3])
    [[0], [0, 1], [0, 1, 2]]
    @TODO should I return a list or a tuple? using * (star operator) is faster than list()
    '''
    return map(lambda size: range(size), column_sizes)

def _tuplesToList(tuples: List[Tuple]) -> List[List[int]]:
    return [*map(lambda xs: [*xs], tuples)]

def _cartesian(lists: List):
    '''
    Given a list of elements
    Returns a list containing the cartesian product between each list
    Example: _cartesian([[0, 1, 2], [0, 1, 2]])
    [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    @TODO should I return a list or a tuple? using * (star operator) is faster than list()
    '''
    return _tuplesToList(product(*lists))

def buildHypergraphComplement(context: Context) -> List[List[int]]:
    '''
    Given a Context k with the form: [[[inc_11, .., inc_1n], .., [inc_n1, .., inc_nr]], d_i, ..., d_k]
    It returns a Hypergraph with the complement of the minimal traversal of the context k
    Example:
    buildHypergraph([[0, 1], [1, 2], [0, 2]], 3, 3)
    [[0, 3], [1, 3], [1, 4], [2, 3], [2, 4], [2, 5]]
    '''
    if len(context) < 2: raise Exception("Context should have at least 2 params: ctx and size of ctx")

    HYPERGRAPH: List[List[int]] = []

    dimension_sizes: List[int] = context[1:]
    dimensions = _dimensions(dimension_sizes)
    C = _cartesian(dimensions)

    for c in C:
        # @todo is this an expensive operation? complement operation in sets
        if c not in context[0]:
            summ = 0
            edges: List[int] = []
            for e, elem in enumerate(c[:-1]):
                curr_summ = summ + elem
                edges.append(curr_summ)
                summ += context[e + 1]

            latest_id = summ + c[len(c) - 1]
            edges.append(latest_id)

            HYPERGRAPH.append(edges)

    return HYPERGRAPH
