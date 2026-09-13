/**
 * Σάρωση directory και παραγωγή normalized tree structure.
 *
 * Η κλάση TreeScanner:
 * - διαβάζει αναδρομικά όλους τους φακέλους
 * - δημιουργεί λεξικό parent → children
 * - χρησιμοποιείται ως input για τον ταξινομητή αρχιτεκτονικής
 *
 * Αποτελεί το πρώτο στάδιο του pipeline αναγνώρισης αρχιτεκτονικής.
 */

import { promises as fs } from "fs";
import path from "path";

export class TreeScanner {
  /**
   * Σκανάρει ένα directory και επιστρέφει το tree structure.
   *
   * Το tree είναι dict: { "root": ["child1", "child2", ...], ... }
   */
  async scan(rootPath: string): Promise<Record<string, string[]>> {
    const tree: Record<string, string[]> = {};

    async function walk(current: string) {
      const entries = await fs.readdir(current, { withFileTypes: true });

      for (const entry of entries) {
        if (entry.isDirectory()) {
          const fullPath = path.join(current, entry.name);
          const parent = current;
          const node = fullPath;

          if (!tree[parent]) {
            tree[parent] = [];
          }
          tree[parent].push(node);

          await walk(fullPath);
        }
      }
    }

    await walk(rootPath);
    return tree;
  }
}
