#!/usr/bin/node
console.log(typeof(process.argv[2]) === 'number' ? 'Not a number' : `My number: ${process.argv[2]}`);
