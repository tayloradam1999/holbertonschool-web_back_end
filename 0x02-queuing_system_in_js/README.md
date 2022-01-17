# 0x02-queuing_system_in_js

## Learning Objectives
- How to run a Redis server on your machine  
- How to run simple operations with the Redis client  
- How to use a Redis client with Node JS for basic operations  
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue
  
## Required Files for the Project
```package.json```  
```
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }
```  
```.babelrc```  
```
{
  "presets": [
    "@babel/preset-env"
  ]
}
```  
``and...```
Don't forget to run ```$ npm install``` to install all dependencies.

## Workflow
- **Step 1**: Create a Redis instance on your machine.
- **Step 2**: Create Node Redis client.
- **Step 3**: Basic Operations with Node Redis client.
- **Step 4**: Async operations with Node Redis client.
- **Step 5**: Advanced Operations with Node Redis client. (Hash values)
- **Step 6**: Node Redis Client publish/subcribe.
- **Step 7**: Kue 'Job creator' queue
- **Step 8**: Kue 'Job processor' queue
- **Step 9**: Track progress and errors with Kue
- **Step 10**: Writing 'job creation' function
- **Step 11**: Writing a test for the job creation function
- **Step 12**: Wrapping everything together to make an 'In stock' app
