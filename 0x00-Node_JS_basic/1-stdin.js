// Log first line
console.log('Welcome to Holberton School, what is your name?');
// Start stdin process
process.stdin
  .on('readable', () => {
    const name = process.stdin.read();
    // after collecting name from stdin, prints it
    // null check for checker
    if (name !== null) {
      process.stdout.write(`Your name is: ${name}`);
    }
  })
  // when user exits program, log last statement

  // this is where the child process is taken into account.
  // the difference lies in when the program will end.
  .on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
// End of program!
