export default function updateUniqueItems(getMap) {
  if (!(getMap instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const [k, v] of getMap) {
    if (v === 1) {
      getMap.set(k, 100);
    }
  }
  return getMap;
}
