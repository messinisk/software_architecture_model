"""_summary_
    """
from software_architecture_model_python.validators.completeness import CompletenessCalculator


def test_completeness_basic():
    """_summary_
    """
    calc = CompletenessCalculator()

    input_tree = {"root": ["a", "b"]}
    canonical_tree = {"root": ["a"]}

    score = calc.calculate(input_tree, canonical_tree)
    assert 0 <= score <= 1
