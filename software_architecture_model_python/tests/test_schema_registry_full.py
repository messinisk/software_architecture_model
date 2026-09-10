from pathlib import Path
import json
from software_architecture_model_python.schemas import SchemaRegistry


def test_load_json(tmp_path):
    reg = SchemaRegistry()

    # Δημιουργούμε προσωρινό JSON αρχείο
    sample_json = tmp_path / "sample.json"
    sample_json.write_text(json.dumps({"a": 1, "b": 2}), encoding="utf-8")

    data = reg.load_json(sample_json)
    assert isinstance(data, dict)
    assert data == {"a": 1, "b": 2}

def test_load_architecture_invalid():
    reg = SchemaRegistry()
    result = reg.load_architecture("INVALID")
    assert result == {}


