#!/usr/bin/node

const file = process.argv[2];
const data = process.argv[3];
const fs = require('fs');

fs.writeFile(file, data, (err) => {
  if (err) { console.log(err); }
});
