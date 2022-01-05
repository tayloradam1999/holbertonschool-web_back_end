// Log first line
console.log('Welcome to Holberton School, what is your name?');
// Start stdin process
process.stdin
  .on('data', (data) => {
    const name = data.toString().trim();
    // after collecting name from stdin, prints it
    console.log('Your name is: %s', name);
  })
  // when user exits program, log last statement
  .on('end', () => {
    console.log('This important software is now closing');
  });
// End of program!
