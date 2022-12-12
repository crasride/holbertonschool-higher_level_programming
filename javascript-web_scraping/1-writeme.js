#!/usr/bin/node
const fs = require('fs');
// that writes a string to a file
fs.writeFileSync(process.argv[2], process.argv[3]);
