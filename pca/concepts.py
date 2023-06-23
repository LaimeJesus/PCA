
from typing import List

from pca.hypergraph import createHypergraphFromContext, Context


def fromHypergraphToConcepts(M: str) -> List[List[str]]:
    """
    Given a Hypergraph string with the following form:
    a11 a12 ... a1n
    b11 b12 ... b1m
    ...
    n11 ...
    It returns
    [['a11', 'a12', ..., 'a1n'], ['b11', 'b12', .., 'b1m'], .. ['n11',..]]
    Hypergraph Example:
    3 5 4
    3 5 1 2
    0 3 4 2
    0 1 2
    4
    0
    0
    0
    2
    2
    Result
    [['3', '5', '4'], ['3', '5', '1', '2'], ['0', '3', '4', '2'], ['0', '1', '2']]
    """
    T = M.split("\n")

    "@TODO it is too restrictive, this condition does not allow the creation of a graph with a single line!"
    if len(T) == 1:
        raise ValueError("M is not an Hypergraph")

    R: List[List[str]] = []
    maxiC = 0
    for x in T:
        c = x.split(" ")
        R.append(c)
        # maxiC is the starting index where the extra nodes needs to be removed from the Concepts
        maxiC = max(maxiC, len(c))

    MAGIC_NUMBER = 3
    for _ in range(maxiC + MAGIC_NUMBER):
        R.pop(len(R)-1)

    return R

def fromTraversalToConcept(traversal: List[str], context: Context):
    BEGIN = 1
    summ = 0
    Concept = []
    for _, value in enumerate(context[BEGIN:]):
        # we can directly use Comp as a set because we does not allow repetition in this container
        Comp = set()
        for e in range(summ, summ + value):
            if str(e) not in traversal:
                # we can directly add this element as a number, because summ is a number and e is a number
                new_element = e - summ
                Comp.add(new_element)
        Concept.append(Comp)
        summ += value

    return Concept

def complementConceptWithTraversals(Concepts: List[List[str]], context: Context):
    # @TODO investigate why does it call traversal instead of concept!
    return map(lambda traversal: fromTraversalToConcept(traversal, context), Concepts)

def createConceptFromContext(context: Context) -> List[List[str]]:
    hypergraph = createHypergraphFromContext(context)
    Concepts = fromHypergraphToConcepts(hypergraph)

    return Concepts
