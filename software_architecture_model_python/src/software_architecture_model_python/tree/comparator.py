"""
Σύγκριση directory trees με canonical αρχιτεκτονικά trees.

Το module παρέχει:
- Jaccard similarity για σύγκριση κόμβων
- DeepDiff για εντοπισμό structural διαφορών
- NetworkX γράφους για αναπαράσταση parent→child σχέσεων

Χρησιμοποιείται από τον ArchitectureClassifier για υπολογισμό ομοιότητας.
"""

import networkx as nx
from deepdiff import DeepDiff


def jaccard(a: set[str], b: set[str]) -> float:
    """
    Υπολογίζει το Jaccard similarity μεταξύ δύο συνόλων κόμβων.

    :param a: Πρώτο σύνολο κόμβων.
    :type a: set[str]
    :param b: Δεύτερο σύνολο κόμβων.
    :type b: set[str]
    :return: Ο δείκτης ομοιότητας Jaccard.
    :rtype: float
    """
    if not a and not b:
        return 1.0
    return len(a & b) / len(a | b)


class TreeComparator:
    """
    Συγκρίνει δύο directory trees:
    - Graph similarity (networkx)
    - Structural diff (deepdiff)
    - Jaccard similarity (folders)
    """

    def build_graph(self, tree: dict[str, list[str]]) -> nx.DiGraph:
        """
    Μετατρέπει ένα directory tree σε γράφο NetworkX.

    :param tree: Λεξικό με parent → children.
    :type tree: dict[str, list[str]]
    :return: Κατευθυνόμενος γράφος που αναπαριστά το tree.
    :rtype: networkx.DiGraph
    """
        g = nx.DiGraph()
        for parent, children in tree.items():
            for child in children:
                g.add_edge(parent, child)
        return g

    def compare(
        self, input_tree: dict[str, list[str]], canonical_tree: dict[str, list[str]]
    ) -> dict[str, float]:
        """
    Συγκρίνει δύο trees και επιστρέφει μετρικές ομοιότητας.

    :param input_tree: Το tree του project.
    :type input_tree: dict[str, list[str]]
    :param canonical_tree: Το canonical tree της αρχιτεκτονικής.
    :type canonical_tree: dict[str, list[str]]
    :return: Μετρικές σύγκρισης (jaccard, missing, extra).
    :rtype: dict[str, float]
    """
        input_graph = self.build_graph(input_tree)
        canonical_graph = self.build_graph(canonical_tree)

        # Structural diff
        diff = DeepDiff(input_tree, canonical_tree, ignore_order=True)

        # Jaccard similarity
        input_nodes = set(input_graph.nodes)
        canonical_nodes = set(canonical_graph.nodes)
        jaccard_score = jaccard(input_nodes, canonical_nodes)

        return {
            "jaccard": jaccard_score,
            "missing": len(diff.get("dictionary_item_removed", {})),
            "extra": len(diff.get("dictionary_item_added", {})),
        }
