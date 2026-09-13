export default function appendToEachArrayValue(array, appendString) {
    let a = 0;
  for (let item of array) {
    array[a] = appendString + item;
    a++;
  }

  return array;
}
