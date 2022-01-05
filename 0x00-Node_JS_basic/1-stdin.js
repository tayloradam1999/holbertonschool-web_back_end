console.log('Welcome to Holberton School, what is your name?');
// User should input name on a new line
process.stdin.on('data', data => {
  // Gather user name from stdin
  const name = data.toString();
  // Log users name
  console.log('Your name is: %s', name);
  process.exit();
});
process.on('exit', data2 => {
  console.log('This important software is now closing');
});
