from software_architecture_model_python.validators import ArchitectureClassifier



def test_best_match(tmp_path):
    root = tmp_path / "proj"
    root.mkdir()
    (root / "controllers").mkdir()
    (root / "models").mkdir()

    clf = ArchitectureClassifier()
    arch, score = clf.best_match(str(root))

    assert isinstance(arch, str)
    assert isinstance(score, float)
