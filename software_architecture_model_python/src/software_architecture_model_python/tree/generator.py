"""
Δημιουργία directory trees για αρχιτεκτονικές (MVC, MVVM, DDD, Event‑Driven, Flow‑Based).

Το module παρέχει την κλάση TreeGenerator, η οποία:
- φορτώνει canonical trees από το SchemaRegistry
- δημιουργεί φακέλους στο filesystem
- δημιουργεί __init__.py σε κάθε φάκελο
- χρησιμοποιείται από το CLI για την εντολή 'sam generate'
"""

from pathlib import Path

from software_architecture_model_python.schemas import SchemaRegistry


class TreeGenerator:
    """
    Generator για directory trees αρχιτεκτονικών.
    """

    def __init__(self) -> None:
        self.registry = SchemaRegistry()

    def _create_folder(self, path: Path) -> Path:
        """
        Δημιουργεί έναν φάκελο και το __init__.py μέσα του.
        Επιστρέφει το path του __init__.py.
        """
        path.mkdir(parents=True, exist_ok=True)
        init_file = path / "__init__.py"
        init_file.touch(exist_ok=True)
        return init_file

    def _create_tree(self, tree: dict[str, list[str]], root: Path) -> list[Path]:
        """
        Δημιουργεί ένα directory tree στο filesystem.
        Επιστρέφει paths προς όλα τα __init__.py αρχεία.
        """
        created_paths: list[Path] = []

        for parent, children in tree.items():
            parent_path = root / Path(parent).name
            created_paths.append(self._create_folder(parent_path))

            for child in children:
                child_path = parent_path / Path(child).name
                created_paths.append(self._create_folder(child_path))

        return created_paths

    def generate(self, architecture: str, output_path: str) -> list[Path]:
        """
        Δημιουργεί το directory tree για μια αρχιτεκτονική.
        """
        canonical_trees = self.registry.load_architecture(architecture)
        root = Path(output_path)

        created: list[Path] = []

        for tree_name, tree in canonical_trees.items():
            arch_root = root / tree_name
            created.append(self._create_folder(arch_root))
            created.extend(self._create_tree(tree, arch_root))

        return created
