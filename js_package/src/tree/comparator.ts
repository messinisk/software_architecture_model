/**
 * Σύγκριση directory trees με canonical αρχιτεκτονικά trees.
 *
 * Παρέχει:
 * - Jaccard similarity για σύγκριση κόμβων
 * - Structural diff (fast-deep-equal)
 * - Graph αναπαράσταση parent → child σχέσεων (graphlib)
 *
 * Χρησιμοποιείται από τον ArchitectureClassifier για υπολογισμό ομοιότητας.
 */

import { Graph } from "graphlib";
import equal from "fast-deep-equal";

/**
 * Υπολογίζει το Jaccard similarity μεταξύ δύο συνόλων κόμβων.
 */
export function jaccard(a: Set<string>, b: Set<string>): number {
  if (a.size === 0 && b.size === 0) {
    return 1.0;
  }
  const intersection = new Set([...a].filter((x) => b.has(x)));
  const union = new Set([...a, ...b]);
  return intersection.size / union.size;
}

export class TreeComparator {
  /**
   * Μετατρέπει ένα directory tree σε γράφο graphlib.
   */
  buildGraph(tree: Record<string, string[]>): Graph {
    const g = new Graph({ directed: true });

    for (const parent of Object.keys(tree)) {
      g.setNode(parent);
      for (const child of tree[parent]) {
        g.setNode(child);
        g.setEdge(parent, child);
      }
    }

    return g;
  }

  /**
   * Συγκρίνει δύο trees και επιστρέφει μετρικές ομοιότητας.
   */
  compare(
    inputTree: Record<string, string[]>,
    canonicalTree: Record<string, string[]>
  ): Record<string, number> {
    const inputGraph = this.buildGraph(inputTree);
    const canonicalGraph = this.buildGraph(canonicalTree);

    // Structural diff (αντίστοιχο του DeepDiff)
    const missing = equal(inputTree, canonicalTree) ? 0 : this.countMissing(inputTree, canonicalTree);
    const extra = equal(inputTree, canonicalTree) ? 0 : this.countExtra(inputTree, canonicalTree);

    // Jaccard similarity
    const inputNodes = new Set(inputGraph.nodes());
    const canonicalNodes = new Set(canonicalGraph.nodes());
    const jaccardScore = jaccard(inputNodes, canonicalNodes);

    return {
      jaccard: jaccardScore,
      missing,
      extra,
    };
  }

  /**
   * Εντοπίζει missing keys όπως το DeepDiff["dictionary_item_removed"].
   */
  private countMissing(
    inputTree: Record<string, string[]>,
    canonicalTree: Record<string, string[]>
  ): number {
    let count = 0;
    for (const key of Object.keys(canonicalTree)) {
      if (!(key in inputTree)) {
        count++;
      }
    }
    return count;
  }

  /**
   * Εντοπίζει extra keys όπως το DeepDiff["dictionary_item_added"].
   */
  private countExtra(
    inputTree: Record<string, string[]>,
    canonicalTree: Record<string, string[]>
  ): number {
    let count = 0;
    for (const key of Object.keys(inputTree)) {
      if (!(key in canonicalTree)) {
        count++;
      }
    }
    return count;
  }
}
