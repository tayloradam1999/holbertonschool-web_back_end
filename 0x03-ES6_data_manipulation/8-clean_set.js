export default function cleanSet(set, startString) {
  if (!startString || !startString instanceof String) {
    return '';
  }
  const myArr = [];
  for (const item of set) {
    if (item.startsWith(startString)) {
      myArr.push(item.slice(startString.length));
    }
  }
  const myStr = myArr.join('-');
  return myStr;
}

//   let myStr = "";
//   set.forEach((v) => myStr.concat(v - startString + '-'));
//   console.log(myStr);
