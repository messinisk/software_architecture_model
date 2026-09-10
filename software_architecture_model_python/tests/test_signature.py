"""_summary_
    """

from software_architecture_model_python.validators import SignatureEngine


def test_signature_engine_load():
    """_summary_
    """
    engine = SignatureEngine()
    signatures = engine.load_signatures()

    assert isinstance(signatures, dict)
    assert "MVC" in signatures
    assert hasattr(signatures["MVC"], "required_nodes")
