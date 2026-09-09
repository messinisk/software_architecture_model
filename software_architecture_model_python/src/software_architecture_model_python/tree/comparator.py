"""missing-module-docstring"""

import networkx as nx
from deepdiff import DeepDiff


def jaccard(a: set[str], b: set[str]) -> float:
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
        g = nx.DiGraph()
        for parent, children in tree.items():
            for child in children:
                g.add_edge(parent, child)
        return g

    def compare(
        self, input_tree: dict[str, list[str]], canonical_tree: dict[str, list[str]]
    ) -> dict[str, float]:
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
