import { fileURLToPath } from "url";
import path from "path";
import { TreeGenerator } from "../src/tree/generator.js";

const filename = fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);

test("TreeGenerator creates architecture folders", async () => {
  const gen = new TreeGenerator();
  const out = path.join(dirname, "output");

  const created = await gen.generate("MVC", out);

  expect(created.length).toBeGreaterThan(0);
});
