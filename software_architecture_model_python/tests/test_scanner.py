"""_summary_
    """
from software_architecture_model_python.tree import TreeScanner


def test_scanner_basic(tmp_path):
    """_summary_

    Args:
        tmp_path (_type_): _description_
    """
    root = tmp_path / "project"
    (root / "a").mkdir(parents=True)
    (root / "b").mkdir(parents=True)

    scanner = TreeScanner()
    tree = scanner.scan(str(root))

    assert str(root) in tree
    assert any("a" in p for p in tree[str(root)])
    assert any("b" in p for p in tree[str(root)])
