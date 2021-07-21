export default function cleanSet(set, startString) {
  if (startString === '') {
    return startString;
  }
  const myArr = [];
  for (const item of set) {
    if (item.startsWith(startString)) {
      myArr.push(item.slice(startString.length));
    }
  }
  return myArr.join('-');
}

//   let myStr = "";
//   set.forEach((v) => myStr.concat(v - startString + '-'));
//   console.log(myStr);
