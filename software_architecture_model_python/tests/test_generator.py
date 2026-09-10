"""_summary_
    """
from pathlib import Path
from software_architecture_model_python.tree import TreeGenerator


def test_tree_generator(tmp_path):
    """_summary_

    Args:
        tmp_path (_type_): _description_
    """
    gen = TreeGenerator()
    output = tmp_path / "generated"

    created = gen.generate("MVC", str(output))

    # created πρέπει να είναι λίστα από φακέλους
    assert isinstance(created, list)
    assert all(isinstance(p, Path) for p in created)

    # κάθε φάκελος πρέπει να έχει __init__.py
    for folder in created:
        init_file = folder / "__init__.py"
        assert init_file.exists()