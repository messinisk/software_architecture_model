import { CompletenessCalculator } from "../src/validators/completeness";

test("calculate completeness", () => {
  const calculator = new CompletenessCalculator();

  const inputTree = {
    src: ["controllers", "models"]
  };

  const canonicalTree = {
    src: ["controllers", "models", "views"]
  };

  const result = calculator.calculate(
    inputTree,
    canonicalTree
  );

  expect(result).toBeGreaterThanOrEqual(0);
  expect(result).toBeLessThanOrEqual(1);
});