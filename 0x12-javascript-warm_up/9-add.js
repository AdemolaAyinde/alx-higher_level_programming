#!/usr/bin/node
function add(a, b) {
  const c = a + b
  console.log(c)
}
//Number(process.argv[2]), Number(process.argv[3]) -  This is used to convert the user input to a number
add(Number(process.argv[2]), Number(process.argv[3]))
