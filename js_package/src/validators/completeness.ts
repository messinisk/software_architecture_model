/**
 * Υπολογισμός πληρότητας ενός project σε σχέση με ένα canonical architecture tree.
 *
 * Το module παρέχει τον CompletenessCalculator, ο οποίος συγκρίνει το input tree
 * με το canonical tree και επιστρέφει ποσοστό πληρότητας.
 */

import { TreeComparator } from "../tree/comparator.js";

export class CompletenessCalculator {
  /**
   * Υπολογίζει την πληρότητα (%) ενός project σε σχέση με το canonical tree.
   */
  calculate(
    inputTree: Record<string, string[]>,
    canonicalTree: Record<string, string[]>
  ): number {
    const comparator = new TreeComparator();

    const comparison = comparator.compare(
      inputTree,
      canonicalTree
    );

    const jaccardScore = comparison.jaccard;
    const missing = comparison.missing;

    // Απλή φόρμουλα πληρότητας
    const completeness =
      Math.max(0, jaccardScore - missing * 0.02);

    return Number(completeness.toFixed(3));
  }
}