import { fileURLToPath } from "url";
import path from "path";
import { SchemaRegistry } from "../src/schemas/registry";

const filename = fileURLToPath(import.meta.url);
const dirname = path.dirname(filename);

test("loadJson loads JSON correctly", async () => {
  const reg = new SchemaRegistry();
  const data = await reg.loadJson(path.join(dirname, "sample.json"));
  expect(typeof data).toBe("object");
});
