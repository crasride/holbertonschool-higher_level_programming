#!/usr/bin/node
// module filesystem and require filesystem
const fs = require('fs');
// readFile
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (data === undefined) {
    console.log(err || data);
  } else {
    console.log(data);
  }
});
