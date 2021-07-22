export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }
  const myArr = [];
  for (const item of set) {
    if (typeof item === 'string' && item.startsWith(startString)) {
      myArr.push(item.slice(startString.length));
    }
  }
  return myArr.join('-');
}
