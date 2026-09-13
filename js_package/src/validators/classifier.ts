/**
 * Ταξινόμηση αρχιτεκτονικής project με βάση canonical trees και signatures.
 *
 * Ο ArchitectureClassifier:
 * - συγκρίνει το input tree με όλες τις διαθέσιμες αρχιτεκτονικές
 * - υπολογίζει Jaccard similarity (TreeComparator)
 * - υπολογίζει Signature similarity (SignatureEngine)
 * - επιστρέφει score ομοιότητας για κάθε αρχιτεκτονική
 */

import { SchemaRegistry } from "../schemas/registry.js";
import { TreeScanner } from "../tree/scanner.js";
import { TreeComparator } from "../tree/comparator.js";
import { SignatureEngine, ArchitectureSignature } from "../validators/signature.js";
import { intersection } from "../utils/set.js";


export class ArchitectureClassifier {
  private registry: SchemaRegistry;
  private scanner: TreeScanner;
  private comparator: TreeComparator;
  private signatures: Record<string, ArchitectureSignature>;

  constructor() {
    this.registry = new SchemaRegistry();
    this.scanner = new TreeScanner();
    this.comparator = new TreeComparator();
    this.signatures = new SignatureEngine().load_signatures();
  }

  /**
   * Υπολογίζει score ομοιότητας για κάθε αρχιτεκτονική.
   */
  async classify(projectPath: string): Promise<Record<string, number>> {
    const inputTree = await this.scanner.scan(projectPath);
    const results: Record<string, number> = {};

    // Extract input nodes once
    const inputNodes = new Set<string>();
    for (const parent of Object.keys(inputTree)) {
      inputNodes.add(parent);
      for (const child of inputTree[parent]) {
        inputNodes.add(child);
      }
    }

    const canonical = await this.registry.loadAll();

    for (const archName of Object.keys(canonical)) {
      // 1) Jaccard score (TreeComparator)
      const comparison = this.comparator.compare(inputTree, canonical[archName]);
      const jaccardScore = comparison.jaccard;

      // 2) Signature score (SignatureEngine)
      const signature = this.signatures[archName];
      const sigScore = this.signature_score(inputNodes, signature);

      // 3) Combine scores
      const finalScore = (jaccardScore * 0.6) + (sigScore * 0.4);

      // 4) Save result
      results[archName] = Number(finalScore.toFixed(3));
    }

    return results;
  }

  /**
   * Επιστρέφει την αρχιτεκτονική με το υψηλότερο score.
   */
  async best_match(projectPath: string): Promise<[string, number]> {
    const scores = await this.classify(projectPath);
    let bestArch = "";
    let bestScore = -1;

    for (const [arch, score] of Object.entries(scores)) {
      if (score > bestScore) {
        bestArch = arch;
        bestScore = score;
      }
    }

    return [bestArch, bestScore];
  }

  /**
   * Υπολογίζει score ομοιότητας με βάση την αρχιτεκτονική υπογραφή (signature).
   */
  private signature_score(
    inputNodes: Set<string>,
    signature: ArchitectureSignature
  ): number {
    const requiredMatch =
      intersection(inputNodes, signature.required_nodes).size /
      Math.max(1, signature.required_nodes.size);

    const optionalMatch =
      intersection(inputNodes, signature.optional_nodes).size /
      Math.max(1, signature.optional_nodes.size);

    return Number(((requiredMatch * 0.7) + (optionalMatch * 0.3)).toFixed(3));
  }
}
