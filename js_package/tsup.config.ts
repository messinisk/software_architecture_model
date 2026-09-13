import { defineConfig } from "tsup";

export default defineConfig({
  entry: ["src/**/*.ts"],
  format: ["esm"],        // ← απαραίτητο για import.meta.url
  sourcemap: true,
  dts: true,
  clean: true,
  outDir: "dist"
});
