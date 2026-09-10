"""_summary_
    """

from software_architecture_model_python.validators import ArchitectureClassifier


def test_classifier_runs(tmp_path):
    """_summary_

    Args:
        tmp_path (_type_): _description_
    """
    root = tmp_path / "proj"
    (root / "controllers").mkdir(parents=True)
    (root / "models").mkdir(parents=True)

    clf = ArchitectureClassifier()
    scores = clf.classify(str(root))

    assert isinstance(scores, dict)
    assert "MVC" in scores
    assert 0 <= scores["MVC"] <= 1
