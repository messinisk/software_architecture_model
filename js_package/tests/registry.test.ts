import { fileURLToPath } from "url";
import path from "path";
import { SchemaRegistry } from "../src/schemas/registry";

const __filename = fileURLToPath('import.meta.url');
const __dirname = path.dirname(__filename);

test("loadJson loads JSON correctly", async () => {
  const reg = new SchemaRegistry();
  const data = await reg.loadJson(path.join(__dirname, "sample.json"));
  expect(typeof data).toBe("object");
});
