"""_summary_
    """

from software_architecture_model_python.schemas import SchemaRegistry


def test_registry_load_all():
    """_summary_
    """
    reg = SchemaRegistry()
    all_arch = reg.load_all()

    assert isinstance(all_arch, dict)
    assert "MVC" in all_arch
    assert isinstance(all_arch["MVC"], dict)
