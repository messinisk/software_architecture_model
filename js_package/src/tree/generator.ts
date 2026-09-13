/**
 * Δημιουργία directory trees για αρχιτεκτονικές (MVC, MVVM, DDD, Event‑Driven, Flow‑Based).
 *
 * Η κλάση TreeGenerator:
 * - φορτώνει canonical trees από το SchemaRegistry
 * - δημιουργεί φακέλους στο filesystem
 * - δημιουργεί __init__.py σε κάθε φάκελο
 * - χρησιμοποιείται από το CLI για την εντολή 'sam generate'
 */

import { fileURLToPath } from "url";
import path from "path";
import { promises as fs } from "fs";
import { SchemaRegistry } from "../schemas/registry.js";

const filename = fileURLToPath("import.meta");
const dirname = path.dirname(filename);

export class TreeGenerator {
  private registry: SchemaRegistry;

  constructor() {
    this.registry = new SchemaRegistry();
  }

  /**
   * Δημιουργεί έναν φάκελο και το __init__.py μέσα του.
   * Επιστρέφει το path του __init__.py.
   */
  private async createFolder(folderPath: string): Promise<string> {
    await fs.mkdir(folderPath, { recursive: true });

    const initFile = path.join(folderPath, "__init__.py");
    await fs.writeFile(initFile, "", { flag: "a" });

    return initFile;
  }

  /**
   * Δημιουργεί ένα directory tree στο filesystem.
   * Επιστρέφει paths προς όλα τα __init__.py αρχεία.
   */
  private async createTree(
    tree: Record<string, string[]>,
    root: string
  ): Promise<string[]> {
    const created: string[] = [];

    for (const parent of Object.keys(tree)) {
      const parentPath = path.join(root, path.basename(parent));
      created.push(await this.createFolder(parentPath));

      for (const child of tree[parent]) {
        const childPath = path.join(parentPath, path.basename(child));
        created.push(await this.createFolder(childPath));
      }
    }

    return created;
  }

  /**
   * Δημιουργεί το directory tree για μια αρχιτεκτονική.
   */
  async generate(architecture: string, outputPath: string): Promise<string[]> {
    const canonicalTrees = await this.registry.loadArchitecture(architecture);
    const root = outputPath;

    const created: string[] = [];

    for (const treeName of Object.keys(canonicalTrees)) {
      const archRoot = path.join(root, treeName);

      created.push(await this.createFolder(archRoot));
      const tree = canonicalTrees[treeName];

      const subPaths = await this.createTree(tree, archRoot);
      created.push(...subPaths);
    }

    return created;
  }
}
