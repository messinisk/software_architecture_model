"""
Μηχανισμός φόρτωσης canonical αρχιτεκτονικών trees από το directory `model/`.

Το module παρέχει την κλάση SchemaRegistry, η οποία:
- εντοπίζει τα JSON αρχεία κάθε αρχιτεκτονικής (MVC, MVVM, DDD, Event‑Driven, Flow‑Based)
- τα φορτώνει σε δομές Python
- τα επιστρέφει στον ταξινομητή αρχιτεκτονικής (ArchitectureClassifier)

Χρησιμοποιείται ως κεντρικό registry για όλα τα canonical trees.
"""

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
        """
    Φορτώνει ένα JSON αρχείο και επιστρέφει το περιεχόμενό του ως dict.

    :param path: Το μονοπάτι του JSON αρχείου.
    :type path: Path
    :return: Τα δεδομένα του JSON ως λεξικό.
    :rtype: dict[str, Any]
    """
        data = json.load(path.open("r", encoding="utf-8"))
        return cast(dict[str, Any], data)

    def load_architecture(self, arch: str) -> dict[str, Any]:
        """
    Φορτώνει όλα τα JSON trees για μια συγκεκριμένη αρχιτεκτονική.

    :param arch: Το όνομα της αρχιτεκτονικής (π.χ. 'MVC').
    :type arch: str
    :return: Λεξικό με όλα τα trees της αρχιτεκτονικής.
    :rtype: dict[str, Any]
    """
        arch_path = self.base_path / arch
        trees: dict[str, Any] = {}

        for json_file in arch_path.glob("*.json"):
            trees[json_file.stem] = self.load_json(json_file)

        return trees

    def load_all(self) -> dict[str, dict[str, Any]]:
        """
    Φορτώνει όλες τις αρχιτεκτονικές και τα canonical trees τους.

    :return: Λεξικό με όλες τις αρχιτεκτονικές και τα trees τους.
    :rtype: dict[str, dict[str, Any]]
    """
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
