"""
Ταξινόμηση αρχιτεκτονικής project με βάση canonical trees και signatures.

Το module παρέχει τον ArchitectureClassifier, ο οποίος συγκρίνει το input tree
με όλες τις διαθέσιμες αρχιτεκτονικές και επιστρέφει score ομοιότητας.
"""

from software_architecture_model_python.schemas.registry import SchemaRegistry
from software_architecture_model_python.tree.comparator import TreeComparator
from software_architecture_model_python.tree.scanner import TreeScanner
from software_architecture_model_python.validators.signature import (
    ArchitectureSignature,
    SignatureEngine,
)


class ArchitectureClassifier:
    """
    Κάνει ταξινόμηση αρχιτεκτονικής:
    - MVC
    - MVVM
    - DDD
    - Event-Driven
    - Flow-Based Architecture
    """

    def __init__(self) -> None:
        self.registry = SchemaRegistry()
        self.scanner = TreeScanner()
        self.comparator = TreeComparator()
        self.signatures = SignatureEngine().load_signatures()

    def classify(self, project_path: str) -> dict[str, float]:
        """
    Υπολογίζει score ομοιότητας για κάθε αρχιτεκτονική.

    :param project_path: Το μονοπάτι του project.
    :type project_path: str
    :return: Λεξικό αρχιτεκτονική → score.
    :rtype: dict[str, float]
    """
        input_tree = self.scanner.scan(project_path)
        results: dict[str, float] = {}

        # Extract input nodes once
        input_nodes = set()
        for parent, children in input_tree.items():
            input_nodes.add(parent)
            input_nodes.update(children)

        for arch_name, canonical_tree in self.registry.load_all().items():
            # 1) Jaccard score (TreeComparator)
            comparison = self.comparator.compare(input_tree, canonical_tree)
            jaccard_score = comparison["jaccard"]

            # 2) Signature score (SignatureEngine)
            signature = self.signatures[arch_name]
            sig_score = self.signature_score(input_nodes, signature)

            # 3) Combine scores
            final_score = (jaccard_score * 0.6) + (sig_score * 0.4)

            # 4) Save result
            results[arch_name] = round(final_score, 3)

        return results

    def best_match(self, project_path: str) -> tuple[str, float]:
        """
    Επιστρέφει την αρχιτεκτονική με το υψηλότερο score.

    :param project_path: Το μονοπάτι του project.
    :type project_path: str
    :return: Ζεύγος (όνομα αρχιτεκτονικής, score).
    :rtype: tuple[str, float]
    """
        scores = self.classify(project_path)
        best = max(scores.items(), key=lambda x: x[1])
        return best

    def signature_score(self, input_nodes: set[str], signature: ArchitectureSignature) -> float:
        """
    Υπολογίζει score ομοιότητας με βάση την αρχιτεκτονική υπογραφή (signature).

    :param input_nodes: Οι κόμβοι του input tree.
    :type input_nodes: set[str]
    :param signature: Η υπογραφή της αρχιτεκτονικής.
    :type signature: ArchitectureSignature
    :return: Score ομοιότητας (0–1).
    :rtype: float
    """
        required_match = len(input_nodes & signature.required_nodes) / max(
            1, len(signature.required_nodes)
        )
        optional_match = len(input_nodes & signature.optional_nodes) / max(
            1, len(signature.optional_nodes)
        )
        return round((required_match * 0.7) + (optional_match * 0.3), 3)
