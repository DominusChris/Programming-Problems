var sum = 0;
for (index = 3; index < 1000; index++){
  if (index%3 === 0 || index%5 === 0){
    sum += index;
  }
}
console.log(sum);
// 233168