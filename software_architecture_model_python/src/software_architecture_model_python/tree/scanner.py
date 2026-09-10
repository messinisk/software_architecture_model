"""
Σάρωση directory και παραγωγή normalized tree structure.

Το module παρέχει την κλάση TreeScanner, η οποία:
- διαβάζει αναδρομικά όλους τους φακέλους
- δημιουργεί λεξικό parent → children
- χρησιμοποιείται ως input για τον ταξινομητή αρχιτεκτονικής

Αποτελεί το πρώτο στάδιο του pipeline αναγνώρισης αρχιτεκτονικής.
"""

from pathlib import Path


class TreeScanner:
    """
    Σκανάρει ένα directory και επιστρέφει ένα normalized tree structure.
    Το tree είναι dict: { "root": ["child1", "child2", ...], ... }
    """

    def scan(self, root_path: str) -> dict[str, list[str]]:
        """
    Σκανάρει ένα directory και επιστρέφει το tree structure.

    :param root_path: Το μονοπάτι του project.
    :type root_path: str
    :return: Λεξικό parent → children.
    :rtype: dict[str, list[str]]
    """
        root = Path(root_path)
        tree: dict[str, list[str]] = {}

        for path in root.rglob("*"):
            if path.is_dir():
                parent = str(path.parent)
                node = str(path)
                tree.setdefault(parent, []).append(node)

        return tree
