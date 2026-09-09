"""missing-module-docstring"""

from pathlib import Path


class TreeScanner:
    """
    Σκανάρει ένα directory και επιστρέφει ένα normalized tree structure.
    Το tree είναι dict: { "root": ["child1", "child2", ...], ... }
    """

    def scan(self, root_path: str) -> dict[str, list[str]]:
        root = Path(root_path)
        tree: dict[str, list[str]] = {}

        for path in root.rglob("*"):
            if path.is_dir():
                parent = str(path.parent)
                node = str(path)
                tree.setdefault(parent, []).append(node)

        return tree
