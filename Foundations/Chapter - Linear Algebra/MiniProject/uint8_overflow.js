const x = new Uint8Array(1);
x[0] = 255;
x[0] = x[0] + 1;
console.log(x[0]);
