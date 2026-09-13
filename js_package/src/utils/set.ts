export function intersection<T>(a: Set<T>, b: Set<T>): Set<T> {
  const out = new Set<T>();
  for (const x of a) {
    if (b.has(x)) out.add(x);
  }
  return out;
}
