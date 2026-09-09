import json
from pathlib import Path
from typing import Any, cast


class SchemaRegistry:
    """
    Φορτώνει όλα τα canonical architecture trees από το repo.
    """

    def __init__(self) -> None:
        self.base_path = Path(__file__).resolve().parent.parent.parent.parent / "model"

    def load_json(self, path: Path) -> dict[str, Any]:
        data = json.load(path.open("r", encoding="utf-8"))
        return cast(dict[str, Any], data)

    def load_architecture(self, arch: str) -> dict[str, Any]:
        arch_path = self.base_path / arch
        trees: dict[str, Any] = {}

        for json_file in arch_path.glob("*.json"):
            trees[json_file.stem] = self.load_json(json_file)

        return trees

    def load_all(self) -> dict[str, dict[str, Any]]:
        architectures = [
            "DDD",
            "Event-Driven",
            "Flow_Based_Architecture",
            "MVC",
            "MVVM",
        ]

        registry: dict[str, dict[str, Any]] = {}

        for arch in architectures:
            registry[arch] = self.load_architecture(arch)

        return registry
