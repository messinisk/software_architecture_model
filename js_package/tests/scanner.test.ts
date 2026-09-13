import { TreeScanner } from "../src/tree/scanner";
import path from "path";

test("TreeScanner scans directories correctly", async () => {
  const scanner = new TreeScanner();
  const root = path.join(__dirname, "sample_project");

  const tree = await scanner.scan(root);

  expect(typeof tree).toBe("object");
  expect(Object.keys(tree).length).toBeGreaterThan(0);
});
