# 0x01-unittests_in_js

Learning how to write unittests in JavaScript using Node.js

Libraries used:
- [mocha](https://mochajs.org/)
- [chai](https://www.chaijs.com/)
- [sinon](https://sinonjs.org/)

## Setup
1. Install Node.js
```
$ sudo apt-get install nodejs
```
2. Initalize a package.json file
```
$ npm init
```
3. Install the dependencies
```
$ npm i -D mocha
$ npm i -D chai
$ npm i -D sinon
$ npm i -D request
```
4. Run tests with `npm test`
```
$ npm test 6-payment_token.js
```

## package.json
This is what your devDependencies in package.json should look like after setting up the project:
```
"devDependencies": {
  "mocha": "^9.1.3",
  "chai": "^4.3.4",
  "sinon": "^12.0.1",
  "request": "^2.88.2",
}
```
request is used in later tasks to make HTTP requests.