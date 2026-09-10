from software_architecture_model_python.validators.signature import SignatureEngine

def test_extract_nodes():
    engine = SignatureEngine()
    tree = {"root": ["a", "b"], "a": ["c"], "b": []}
    nodes = engine.extract_nodes(tree)
    assert nodes == {"root", "a", "b", "c"}

def test_compute_depth():
    engine = SignatureEngine()
    tree = {"root": ["a"], "a": ["b"], "b": []}
    depth = engine.compute_depth(tree)
    assert depth == 0

def test_extract_patterns():
    engine = SignatureEngine()
    tree = {"root": ["a", "b"], "a": ["c"], "b": []}
    patterns = engine.extract_patterns(tree)
    assert patterns == {"root->a", "root->b", "a->c"}

def test_build_signature():
    engine = SignatureEngine()
    trees = {
        "mvc_tree": {
            "root": ["controllers", "models"],
            "controllers": [],
            "models": []
        }
    }
    sig = engine.build_signature(trees)
    assert sig.required_nodes == {"root", "controllers", "models"}
    assert isinstance(sig.depth, int)

