
import { TreeComparator } from "../src/tree/comparator";

test("Jaccard similarity works", () => {
  const cmp = new TreeComparator();
  const result = cmp.compare(
    { "a": ["b"] },
    { "a": ["b"] }
  );
  expect(result.jaccard).toBe(1.0);
});
