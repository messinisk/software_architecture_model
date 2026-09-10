"""
Υποσύστημα δημιουργίας αρχιτεκτονικών υπογραφών (signatures).

Το module παρέχει:
- ArchitectureSignature: δομή υπογραφής
- SignatureEngine: μηχανή εξαγωγής canonical signatures από JSON trees
"""

from typing import Any

from software_architecture_model_python.schemas.registry import SchemaRegistry


class ArchitectureSignature:
    """
    Αρχιτεκτονική υπογραφή:
    - required_nodes: κόμβοι που πρέπει να υπάρχουν
    - optional_nodes: κόμβοι που συχνά υπάρχουν
    - depth: μέσο βάθος δέντρου
    - patterns: δομικά μοτίβα (π.χ. controller->view)
    """

    def __init__(
        self,
        required_nodes: set[str],
        optional_nodes: set[str],
        depth: int,
        patterns: set[str],
    ) -> None:
        self.required_nodes = required_nodes
        self.optional_nodes = optional_nodes
        self.depth = depth
        self.patterns = patterns


class SignatureEngine:
    """
    Δημιουργεί canonical signatures για κάθε αρχιτεκτονική.
    """

    def __init__(self) -> None:
        self.registry = SchemaRegistry()

    def extract_nodes(self, tree: dict[str, Any]) -> set[str]:
        """
    Εξάγει όλους τους κόμβους (φακέλους) από ένα directory tree.

    :param tree: Το tree parent → children.
    :type tree: dict[str, Any]
    :return: Σύνολο κόμβων.
    :rtype: set[str]
    """
        nodes: set[str] = set()
        for parent, children in tree.items():
            nodes.add(parent)
            nodes.update(children)
        return nodes

    def compute_depth(self, tree: dict[str, Any]) -> int:
        """
    Υπολογίζει το μέσο βάθος του tree.

    :param tree: Το tree parent → children.
    :type tree: dict[str, Any]
    :return: Μέσο βάθος.
    :rtype: int
    """
        depths = []
        for parent, children in tree.items():
            parent_depth = parent.count("/")
            depths.append(parent_depth)
            for child in children:
                depths.append(child.count("/"))
        return int(sum(depths) / max(1, len(depths)))

    def extract_patterns(self, tree: dict[str, Any]) -> set[str]:
        """
    Εξάγει δομικά μοτίβα parent→child από το tree.

    :param tree: Το tree parent → children.
    :type tree: dict[str, Any]
    :return: Σύνολο μοτίβων.
    :rtype: set[str]
    """
        patterns: set[str] = set()
        for parent, children in tree.items():
            for child in children:
                parent_name = parent.split("/")[-1]
                child_name = child.split("/")[-1]
                patterns.add(f"{parent_name}->{child_name}")
        return patterns

    def build_signature(self, trees: dict[str, Any]) -> ArchitectureSignature:
        """
    Δημιουργεί canonical signature από όλα τα trees μιας αρχιτεκτονικής.

    :param trees: Λεξικό με canonical trees.
    :type trees: dict[str, Any]
    :return: Η αρχιτεκτονική υπογραφή.
    :rtype: ArchitectureSignature
    """
        all_nodes: list[set[str]] = []
        all_patterns: list[set[str]] = []
        depths: list[int] = []

        for tree in trees.values():
            nodes = self.extract_nodes(tree)
            patterns = self.extract_patterns(tree)
            depth = self.compute_depth(tree)

            all_nodes.append(nodes)
            all_patterns.append(patterns)
            depths.append(depth)

        # Required nodes = intersection όλων των canonical trees
        required_nodes = set.intersection(*all_nodes) if all_nodes else set()

        # Optional nodes = union - required
        optional_nodes = set.union(*all_nodes) - required_nodes if all_nodes else set()

        # Depth = μέσος όρος
        avg_depth = int(sum(depths) / max(1, len(depths)))

        # Patterns = union όλων
        pattern_union = set.union(*all_patterns) if all_patterns else set()

        return ArchitectureSignature(
            required_nodes=required_nodes,
            optional_nodes=optional_nodes,
            depth=avg_depth,
            patterns=pattern_union,
        )

    def load_signatures(self) -> dict[str, ArchitectureSignature]:
        """
    Φορτώνει signatures για όλες τις αρχιτεκτονικές.

    :return: Λεξικό αρχιτεκτονική → signature.
    :rtype: dict[str, ArchitectureSignature]
    """
        signatures: dict[str, ArchitectureSignature] = {}
        all_arch = self.registry.load_all()

        for arch_name, trees in all_arch.items():
            signatures[arch_name] = self.build_signature(trees)

        return signatures
