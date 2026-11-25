// The Daily Globe - news-image-20261125 entry program (Node 22, stdlib only).
//
// The entry image sits beside this file as entry.png; the program copies it
// to the grader's output directory as entry.png. Locally, MAKEFUN_OUTPUT_DIR
// stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// Both grader runs copy the same source file, so the output bytes are
// identical every run.

import { copyFileSync, statSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = new URL("./entry.png", import.meta.url);
const target = join(outDir, "entry.png");

copyFileSync(source, target);

// Sanity check: the copied file must be non-empty (the gate wants a whole
// PNG of at most 1 MiB); fail loudly rather than submit an empty output.
const size = statSync(target).size;
if (size === 0 || size > 1_048_576) {
  throw new Error(`entry.png copy has unexpected size: ${size} bytes`);
}
