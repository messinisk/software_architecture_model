from software_architecture_model_python.tree.comparator import TreeComparator


class CompletenessCalculator:
    """
    Υπολογίζει την πληρότητα ενός project σε σχέση με ένα canonical tree.
    """

    def calculate(self, input_tree: dict, canonical_tree: dict) -> float:
        comparator = TreeComparator()
        comparison = comparator.compare(input_tree, canonical_tree)

        jaccard_score = comparison["jaccard"]
        missing = comparison["missing"]

        # Απλή φόρμουλα πληρότητας
        completeness = max(0.0, jaccard_score - (missing * 0.02))
        return round(completeness, 3)
