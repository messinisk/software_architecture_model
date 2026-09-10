from software_architecture_model_python.tree import TreeGenerator
from pathlib import Path
import pytest

def test_create_folder(tmp_path):
    gen = TreeGenerator()
    folder = tmp_path / "x"
    init_file = gen._create_folder(folder)
    assert init_file.exists()
    assert init_file.name == "__init__.py"

def test_create_tree(tmp_path):
    gen = TreeGenerator()
    tree = {"root": ["a", "b"], "a": ["c"], "b": []}
    created = gen._create_tree(tree, tmp_path)
    assert len(created) >= 4
    for f in created:
        assert f.exists()

def test_generate_invalid_architecture(tmp_path):
    gen = TreeGenerator()
    result = gen.generate("INVALID", str(tmp_path))
    assert result == []


