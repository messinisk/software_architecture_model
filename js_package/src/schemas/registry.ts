/**
 * Μηχανισμός φόρτωσης canonical αρχιτεκτονικών trees από το directory `model/`.
 *
 * Η κλάση SchemaRegistry:
 * - εντοπίζει τα JSON αρχεία κάθε αρχιτεκτονικής (MVC, MVVM, DDD, Event‑Driven, Flow‑Based)
 * - τα φορτώνει σε δομές JS/TS
 * - τα επιστρέφει στον ταξινομητή αρχιτεκτονικής
 *
 * Χρησιμοποιείται ως κεντρικό registry για όλα τα canonical trees.
 */
import { fileURLToPath } from "node:url";
import path from "path";
import { promises as fs } from "fs";

const __filename = fileURLToPath('import.meta.url');
const __dirname = path.dirname(__filename);

export class SchemaRegistry {
  private basePath: string;

  constructor() {
    this.basePath = path.resolve(__dirname, "../../../model");
  }

  async loadJson(filePath: string): Promise<Record<string, any>> {
    const raw = await fs.readFile(filePath, "utf-8");
    return JSON.parse(raw);
  }

  async loadArchitecture(arch: string): Promise<Record<string, any>> {
    const archPath = path.join(this.basePath, arch);
    const entries = await fs.readdir(archPath);

    const trees: Record<string, any> = {};

    for (const file of entries) {
      if (file.endsWith(".json")) {
        const fullPath = path.join(archPath, file);
        const stem = path.basename(file, ".json");
        trees[stem] = await this.loadJson(fullPath);
      }
    }

    return trees;
  }

  async loadAll(): Promise<Record<string, Record<string, any>>> {
    const architectures = [
      "DDD",
      "Event-Driven",
      "Flow_Based_Architecture",
      "MVC",
      "MVVM"
    ];

    const registry: Record<string, Record<string, any>> = {};

    for (const arch of architectures) {
      registry[arch] = await this.loadArchitecture(arch);
    }

    return registry;
  }
}
