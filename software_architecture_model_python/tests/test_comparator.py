"""_summary_
    """

from software_architecture_model_python.tree.comparator import TreeComparator


def test_comparator_jaccard():
    """_summary_
    """
    comp = TreeComparator()
    a = {"root": ["a", "b"]}
    b = {"root": ["a"]}

    result = comp.compare(a, b)
    assert 0 <= result["jaccard"] <= 1
    assert result["missing"] >= 0
    assert result["extra"] >= 0
