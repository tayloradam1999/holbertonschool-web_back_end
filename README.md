## Trimester 4 - Back-End Web Development
  
All of the concept based Back-End Web Development projects for Holberton School Tulsa  
  
## [0x00-ES6_basic](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x00-ES6_basic)  
  
![](./readme_assets/08806026ef621f900121.png)
  
JavaScript ES6 (also known as ECMAScript 2015 or ECMAScript 6) is the newer version of JavaScript that was introduced in 2015.
  
[EMCAScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Language_Resources) is the standard that JavaScript programming language uses. ECMAScript provides the specification on how JavaScript programming language should work.  
  
A list of all of the changes from the ES6 update can be found [here](https://www.javascripttutorial.net/es6/), but for this project we will only focus on the following learning objectives.
  
<hr>
  
### Learning Objectives
- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and for-of loops
  
## [0x00-Node_JS_basic](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x00-Node_JS_basic)
  
Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser. Node.js lets developers use JavaScript to write command line tools and for server-side scripting—running scripts server-side to produce dynamic web page content before the page is sent to the user's web browser.  

Consequently, Node.js represents a "JavaScript everywhere" paradigm, unifying web-application development around a single programming language, rather than different languages for server-side and client-side scripts.  
  
<hr>
  
### Learning Objectives
- run javascript using NodeJS
- use NodeJS modules
- use specific Node JS module to read files
- use ```process``` to access command line arguments and the environment
- create a small HTTP server using Node JS
- create a small HTTP server using Express JS
- create advanced routes with Express JS
- use ES6 with Node JS with Babel-node
- use Nodemon to develop faster  
  
<hr>
  
Below is an **example** of a simple Express application.
  
```javascript
const express = require('express');
const app = express();


app.get('/', (req, res) => {
  res.send('Hello World!');
});


app.listen(3000, () => {
  console.log('Example app listening on port 3000!');
});
```
  
## [0x00-Unittests_and_integration_tests](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x00-Unittests_and_integration_tests)  
  
Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.
  
The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?
  
Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.
  
Integration tests will test interactions between every part of your code.

<hr>

### Learning Objectives
- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures

<hr>
  
Here is a great **example** of a program that tests that a file was deleted properly:
  
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm

import os.path
import tempfile
import unittest

class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wb") as f:
            f.write("Delete me!")
        
    def test_rm(self):
        # remove the file
        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")
```

## [0x00-caching](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x00-caching)  
  
In this project, you learn different caching algorithms.
  
### Resources
**Read or watch:**
- [Cache replacement policies - FIFO](https://intranet.hbtn.io/rltoken/Y0L874YNAlGVhRYvk2bj6g)
- [Cache replacement policies - LIFO](https://intranet.hbtn.io/rltoken/f_-9S9RJVleXhOzvyWGF4w)
- [Cache replacement policies - LRU](https://intranet.hbtn.io/rltoken/vpByVJ0WslpU_faf4sL0lg)
- [Cache replacement policies - MRU](https://intranet.hbtn.io/rltoken/n0jYunLhh2RAmcfKAtk94Q)
- [Cache replacement policies - LFU](https://intranet.hbtn.io/rltoken/9XAMz_nm40yOo9ss6nRQfw)
  
### Learning Objectives
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

### Python Scripts Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using ```python3``` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly ```#!/usr/bin/env python3```
- ```A README.md``` file, at the root of the folder of the project, is mandatory
- Your code should use the ```pycodestyle``` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using ```wc```
- All your modules should have a documentation (```python3 -c 'print(__import__("my_module").__doc__)'```)
- All your classes should have a documentation (```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```)
- All your functions (inside and outside a class) should have a documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__```)' and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```)
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

## [0x00-python_variable_annotations](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x00-python_variable_annotations)
  
Typing defines a standard notation for Python function and variable type annotations. The notation can be used for documenting code in a concise, standard format, and it has been designed to also be used by static and runtime type checkers, static analyzers, IDEs and other tools.  
  
<hr>  
  
### Learning Objectives
- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with ```mypy```
  
<hr>
  
Here is an **exmaple** of variable annotations at use:
  
```python
from typing import List

def should_use(annotations: List[str]) -> bool:
    print("They're awesome!")
    return True
```
  
## [0x00-redis_basic](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x00-redis_basic)  
  
Redis is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine. Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams. Redis has built-in replication, Lua scripting, LRU eviction, transactions, and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.  
  
You can run **atomic operations** on these types, like appending to a string; incrementing the value in a hash; pushing an element to a list; computing set intersection, union and difference; or getting the member with highest ranking in a sorted set.  
  
To achieve top performance, Redis works with an in-memory dataset. Depending on your use case, Redis can persist your data either by periodically dumping the dataset to disk or by appending each command to a disk-based log. You can also disable persistence if you just need a feature-rich, networked, in-memory cache.  
  
Redis supports asynchronous replication, with fast non-blocking synchronization and auto-reconnection with partial resynchronization on net split.  
  
<hr>
  
### Learning Objectives

- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache
  
<hr>
  
Here is an example of a script that connects to Redis:
  
```javascript

const redis = require('redis');
const client = redis.createClient({
    host: '<hostname>',
    port: <port>,
    password: '<password>'
});

client.on('error', err => {
    console.log('Error ' + err);
});
```
  
## [0x01-ES6_promise](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x01-ES6_promise)
  
A ```Promise``` is a proxy for a value not necessarily known when the promise is created. It allows you to associate handlers with an asynchronous action's eventual success value or failure reason. This lets asynchronous methods return values like synchronous methods: instead of immediately returning the final value, the asynchronous method returns a promise to supply the value at some point in the future.
  
A ```Promise``` is in one of these states:
- *pending*: initial state, neither fulfilled nor rejected.
- *fulfilled*: meaning that the operation was completed successfully.
- *rejected*: meaning that the operation failed.

A pending promise can either be *fulfilled* with a value or *rejected* with a reason (error). When either of these options happens, the associated handlers queued up by a promise's ```then``` method are called. If the promise has already been fulfilled or rejected when a corresponding handler is attached, the handler will be called, so there is no race condition between an asynchronous operation completing and its handlers being attached.
  
As the ```Promise.prototype.then()``` and ```Promise.prototype.catch()``` methods return promises, they can be chained.
  
<hr>
  
### Learning Objectives
- Promises (how, why, and what)
- How to use the ```then```, ```resolve```, ```catch``` methods
- How to use every method of the Promise object
- Throw / Try
- The await operator
- How to use an async function
  
<hr>
  
Here is an example of a promise:
  
```javascript
const promise = new Promise((resolve, reject) => {
    // do something
    if (success) {
        resolve(value);
    } else {
        reject(error);
    }
});
```

## [0x01-MySQL_Advanced](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x01-MySQL_Advanced)
  
```MYSQL```, the most popular Open Source SQL database management system, is developed, distributed, and supported by Oracle Corporation.
  
The MySQL [website](http://www.mysql.com/) provides the latest information about MySQL software.  
  
<hr>

### Learning Objectives
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL
- [Stored Procedure](https://intranet.hbtn.io/rltoken/XSLEXZ6DC1FZpKEguU5zLQ)
- [Triggers](https://intranet.hbtn.io/rltoken/jp4hJB38DK5cvggzRjPFZg)
- [Views](https://intranet.hbtn.io/rltoken/657QAaSxDHR9TEN3-SjFng)
- [Functions and Operators](https://intranet.hbtn.io/rltoken/2pNgl9CAhuBmyqVEUEmMtg)
- [Trigger Syntax and Examples](https://intranet.hbtn.io/rltoken/aM9l2NvMUqYKIVdXyhEuEw)
- [CREATE TABLE Statement](https://intranet.hbtn.io/rltoken/D7Y3UN5izR-1Li6UH8OrZQ)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://intranet.hbtn.io/rltoken/gKUwpC7nu5GEBA5ra8K6vw)
- [CREATE INDEX Statement](https://intranet.hbtn.io/rltoken/Z8WOMz3RyeUBYAkMqA8Q5g)
- [CREATE VIEW Statement](https://intranet.hbtn.io/rltoken/SEWG9e5zbFrIOr361POJGQ)
  
<hr>
  
Here is an example of a ```MySQL``` script:
  
```SQL
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
  
## [i8n](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x01-i18n)
  
Internationalization (i18n) is the **process of preparing software so that it can support local languages and cultural settings**. An internationalized product supports the requirements of local markets around the world, functioning more appropriately based on local norms and better meeting in-country user expectations.
  
<hr>
  
### Learning Objectives
- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings or request headers
- Learn how to localize timestamps
  
<hr>

Here is an **example** of a python script that identifies the user's locale and timezone, handles the translations and displays the data accordingly:
  
```python
#!/usr/bin/env python3
"""
Basic babel flask app.
Uses Config to set Babel's default local <en>
and timezone <UTC>
Uses that class as config for flask app.
"""
from flask import Flask, request, g
from flask_babel import Babel
from flask_babel import gettext as _
import pytz
from flask.templating import render_template


# Set up Flask app and tend to baby checker
app = Flask(__name__)
babel = Babel(app)
_.__doc__ = "Nice one, checker."
""" Tend to Turlay """


# simulate database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Simple Class to set Babel's default local and timezone
class Config():
    """
    Configure Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Configure Flask
app.config.from_object(Config)


# Determins if en or fr
@babel.localeselector
def get_locale():
    """
    Get locale from request.
    Use a <user>'s preferred local if it is supported
    Order of priority:
        - Locale from URL parameters
        - Locale from user settings
        - Locale from request header
        - Default locale
    """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    try:
        user = get_user()
        if user and user['locale'] in Config.LANGUAGES:
            return user['locale']
        raise Exception
    except Exception:
        return request.accept_languages.best_match(Config.LANGUAGES)


# uses same logic as locale selector but for timezone
@babel.timezoneselector
def get_timezone():
    """
    Find timezone parameter in URL
    Find time zone from user settings
    Default to UTC
    Validate valid time zones. Uses pytz.timezone to catch
    pytz.exceptions.UnknownTimeZoneError
    """
    timezone = request.args.get('timezone')
    if timezone:
        return timezone
    try:
        user = get_user()
        if user and user['timezone'] in pytz.all_timezones:
            return user['timezone']
        raise pytz.exceptions.UnknownTimeZoneError
    except pytz.exceptions.UnknownTimeZoneError:
        return 'UTC'

# simulate getting user from databse
def get_user():
    """
    Returns user dictionary or None if ID cannot be found or
    if <login_as> was not passed.
    """
    user_id = request.args.get('login_as')
    if not user_id:
        return None
    try:
        user_id = int(user_id)
        if user_id < 1 or user_id > 4:
            raise Exception
    except Exception:
        return None
    return users[user_id]


# loads user before page is rendered, ignore empty line below :(

@app.before_request
def before_request():
    """
    Uses get_user() to find a user, if any, and set it as g.user.
    """
    data = get_user()
    if data:
        g.user = data
        home_text = _("You are logged in as %(name)s.", name=data['name'])
        return render_template('5-index.html', home_text=home_text)
    else:
        return render_template('5-index.html', home_text=_('not_logged_in'))


# index page
@app.route('/')
def index():
    """
    Return the index page.
    """
    return render_template('5-index.html')


# run app
if __name__ == '__main__':
    app.run()
```
  
## [0x01-pagination](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x01-pagination)
  
Pagination is the method of separating digital content into different pages on a website. Users can navigate between these pages by clicking links, often in the form of numbers located at the bottom of a page. Paginated content is typically related by some common theme or purpose.
  
<hr>
  
### Learning Objectives
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner
  
<hr>

Here is an **example** of a couple basic python functions that handle returning the paginated
rows of a dataset:
  
```python
#!/usr/bin/env python3
"""
Contains functions that handle
pagination of a dataset.
"""
from typing import Union, Tuple, List
import csv


def index_range(page: int, page_size: int) -> Union[Tuple[int, int], None]:
    """
    -Returns a tuple of size 2 containing a start index and an end index
    corresponding to the page and page_size parameters.
    -Page numbers are 1 -indexed, the first page is page 1.
    """
    if page and page_size:
        return (page * page_size - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        - Returns a list of lists that represent all of the rows
		in the dataset that fall within the range of indexes specified
		- If list is empty, then the page does not exist.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        if start >= len(self.dataset()):
            return []

        return self.dataset()[start:end]
```
  
## [0x01-python_async_function](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x01-python_async_function)  
  
```asyncio``` is a library to write concurrent code using the async/await syntax.
  
```asyncio``` is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
  
asyncio is often a perfect fit for IO-bound and high-level structured network code.
  
<hr>
  
### Learning Objectives
- ```async``` and ```await``` syntax
- How to execute an async program with ```asyncio```
- How to run concurrent coroutines
- How to create ```asyncio``` tasks
- How to use the random module
  
<hr>
  
Here is an **example** of a python script that measures the runtime of a function asynchronously:
  
```python
#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time.
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of wait_n(n, max_delay)"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
```
  
## [0x01-unittests_in_js](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x01-unittests_in_js)
  
#### Mocha
  
**[Mocha](https://mochajs.org/)** is a feature-rich JavaScript test framework running on Node.js and in the browser. It encapsulates tests in test suites (describe-block) and test cases (it-block).
  
Mocha has lots of interesting features:
  
- browser support
- simple async support, including promises
- test coverage reporting
- async test timeout support
- ```before```, ```after```, ```beforeEach```, ```afterEach``` Hooks, etc.
  
#### Chai
  
To make equality checks or compare expected results against actual results we can use Node.js built-in assertion module. However, when an error occurs the test cases will still pass. So Mocha recommends using other assertion libraries and for this tutorial, we will be using **[Chai](https://www.chaijs.com/)**.
  
Chai exposes three assertion interfaces: expect(), assert() and should(). Any of them can be used for assertions.
  
#### Sinon
  
Often, the method that is being tested is required to interact with or call other external methods. Therefore you need a utility to spy, stub, or mock those external methods. This is exactly what **[Sinon](https://sinonjs.org/)** does for you.
  
Stubs, mocks, and spies make tests more robust and less prone to breakage should dependent codes evolve or have their internals modified.
  
<hr>
  
### Learning Objectives
- How to use Mocha to write a test suite
- How to use different assertion libraries (Node or Chai)
- How to present long test suites
- When and how to use spies
- When and how to use stubs
- What are hooks and when to use them
- Unit testing with Async functions
- How to write integration tests with a small node server
  
<hr>
  
Here is an **example** of Mocha test suite:
  
```javascript
// begin a test suite of one or more tests
describe('#sum()', function() {

  // add a test hook
  beforeEach(function() {
    // ...some logic before each test is run
  })
  
  // test a functionality
  it('should add numbers', function() {
    // add an assertion
    expect(sum(1, 2, 3, 4, 5)).to.equal(15);
  })
  
  // ...some more tests
  
})
```
  
## [0x02-ES6_classes](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x02-ES6_classes)
  
ES6 Classes formalize the common JavaScript pattern of simulating class-like inheritance hierarchies using functions and prototypes. They are effectively simple sugaring over prototype-based OO, offering a convenient declarative form for class patterns which encourage interoperability.
  
Classes (as shipped in Chrome) support prototype-based inheritance, constructors, super calls, instance and static methods. The samples included in this demo are:
  
- Creating a new class (declaration-form)
- Creating a new class (expression-form)
- Extending an existing class
- Subclassing methods of a parent class
- Defining static methods
- Subclassing built-ins
  
<hr>
  
### Learning Objectives
- How to define a Class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols
  
<hr>
  
Here is an **example** of a class in JavaScript:
  
```javascript
class Person {
  constructor(name) {
	this.name = name;
  }
  
  sayName() {
	console.log(this.name);
  }
}
```
  
## [0x02-NoSQL](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x02-NoSQL)
  
MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License (SSPL).  
  
<hr>
  
### Learning Objectives
- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB
  
<hr>
  
Here is an **example** of a Javascript program that connects to a MongoDB database:
  
```javascript
const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');


// Connection URL
const url = 'mongodb://localhost:27017';


// Database Name
const dbName = 'myproject';


// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected successfully to server");

  const db = client.db(dbName);

  client.close();
});
```
  
## [0x02-personal_data](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x02-personal_data)
  
Personally identifiable information is defined by the U.S. government as:
  
“Information which can be used to distinguish or trace an individual's identity, such as their name, social security number, biometric records, etc. alone, or when combined with other personal or identifying information which is linked or linkable to a specific individual, such as date and place of birth, mother's maiden name, etc.”
  
*Let's hide this data from those pesky hackers!*
  
<hr>
  
### Learning Objectives
- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables
  
<hr>
  
Here is an **example** of a python script that utilizes ```bcrypt``` to encrypt a password:
  
```python
#!/usr/bin/env python3
"""
Use <bcrypt> to perform hasing on password
Use <bcrypt> to validate password
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns salted, hashed byte string password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates password
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
```
  
## [0x02-python_async_comprehension](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x02-python_async_comprehension)
  
Python has extensive support for synchronous comprehensions, allowing to produce lists, dicts, and sets with a simple and concise syntax. We propose implementing similar syntactic constructions for the asynchronous code.
  
To illustrate the readability improvement, consider the following example:
  
```python
result = []
async for i in aiter():
    if i % 2:
        result.append(i)
```
  
With the proposed asynchronous comprehensions syntax, the above code becomes as short as:
  
```python
result = [i async for i in aiter() if i % 2]
```
  
The PEP also makes it possible to use the await expressions in all kinds of comprehensions:
  
```python
result = [await fun() for fun in funcs]
```
  
### Learning Objectives
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators
  
<hr>
  
Here is an **example** of an asynchronous generator that loops 10 times and each time, asynchronously waits 1 second then yields a random number between 0 and 10:
  
```python
#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
"""
import random
import asyncio
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```
  
### [0x02-queuing_systems_in_js](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x02-queuing_system_in_js)
  
Technologies used:
- [Babel](https://babeljs.io/)
- [Node.js](https://nodejs.org/)
- [Express](https://expressjs.com/)
- [Redis](https://redis.io/)
- [Kue](https://github.com/Automattic/kue)

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
*Side note: This project was issued many years ago and many of my devDependencies have later versions than the ones listed here.*
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
**AND...** 
Don't forget to run ```$ npm install``` to install all dependencies.

## Workflow
- **Step 1**: Create a Redis instance on your machine
- **Step 2**: Create Node Redis client
- **Step 3**: Basic Operations with Node Redis client
- **Step 4**: Async operations with Node Redis client
- **Step 5**: Advanced Operations with Node Redis client (Hash values)
- **Step 6**: Node Redis Client publish/subcribe
- **Step 7**: Kue 'Job creator' queue
- **Step 8**: Kue 'Job processor' queue
- **Step 9**: Track progress and errors with Kue
- **Step 10**: Writing 'job creation' function
- **Step 11**: Writing a test for the job creation function
- **Step 12**: Wrapping everything together to make an 'In stock' Express app
  
## [0x03-Basic_authentication](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x03-Basic_authentication)
  
In this project, you will learn what the authentication process means and implement a ((Basic Authentication)) on a simple API.
  
In the industry, you should not implement your own **Basic authentication** system and use a module or framework that doing it for you (like in Python-Flask: ```Flask-HTTPAuth```). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.
  
![](./readme_assets/6ccb363443a8f301bc2bc38d7a08e9650117de7c.png)
  
<hr>
  
### Learning Objectives
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header
  
<hr>
  
Here is an **example** of a python function that returns what Authorization header should be sent to the server:
  
```python
 def authorization_header(self, request=None) -> str:
        """
        HTTP header authorization
        Args:
            request(Flask.request): The request object
            asdasd
        Returns:
            If <request> is None, returns None.
            If <request> doesn't contain the header key <'Authorization'>,
            returns None.
            Otherwise, returns the value of the header key <'Authorization'>.
        """
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')
```
  
## [0x03-ES6_data_manipulation](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x03-ES6_data_manipulation)
  
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
  
- How to use map, filter and reduce on arrays
- Typed arrays
- The Set, Map, and Weak link data structures
  
<hr>
  
Here is an **example** of a Javascript function that only returns the given values from an array:
  
```javascript
export default function hasValuesFromArray(set, array) {
  const array2 = Array.from(set);
  if (array.every((elem) => array2.includes(elem))) {
    return true;
  }
  return false;
}
```
  
## [0x04-Session_authentication](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x04-Session_authentication)
  
In this project, you will implement a **Session Authentication**. You are not allowed to install any other module.

In the industry, you should not implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: ```Flask-HTTPAuth```). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.
  
<hr>
  
### Learning Objectives
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies
  
<hr>
  
Here is an **example** of a python script that handles session authentication via cookies:
  
```python
#!/usr/bin/env python3
"""
Session Authentication Module
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid
from os import getenv


class SessionAuth(Auth):
    """
    Handles Session Authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a <user_id>
        Args:
            user_id (str): The user's ID
        Returns:
            None if <user_id> is None
            None if <user_id> is not a string
            Otherwise:
                Generates a session ID using the `uuid` module and
                    uuid4() like <id> in <Base>
                Uses new session ID as key of the dict <user_id_by_session_id>,
                    the value for this key must be <user_id>
                Returns the session ID
        The same <user_id> can have multiple session IDs. The <user_id> is
            the value in the dictionary <user_id_by_session_id>
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        # assigns session_id to key, user_id to value
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the user ID for a <session_id>
        Uses .get() to get the value for the key <session_id> in
        <user_id_by_session_id>
        Args:
            session_id (str): The session ID
        Returns:
            None if <session_id> is None
            None if <session_id> is not a string
            The value (The user ID) for the key <session_id> in
                <user_id_by_session_id>
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        my_session_id = self.user_id_by_session_id.get(session_id)
        return my_session_id

    def current_user(self, request=None):
        """
        Returns the <User> instance based on a cookie value
        Uses self.session_cookie(...) and self.user_id_for_session_id(...)
            to return the User ID based on the cookie <_my_session_id>
        By using this new User ID, you will be able to retrieve a <User>
            instance from the database. (You can use User.get())
        Args:
            request: request object
        Returns:
            User instance based on a cookie value
        """
        _my_session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(_my_session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout
        Args:
            request: request object
        Returns:
            If request is None, return False
            if request doesn't contain the session ID, return False
            if the session ID is not linked to any user ID, return False
            Otherwise, delete in <self.user_id_by_session_id> the key
                <session_id> and return True
        """
        if request is None:
            return False
        _my_session_id = self.session_cookie(request)
        if _my_session_id is None:
            return False
        user_id = self.user_id_for_session_id(_my_session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[_my_session_id]
        return True
```
  
## [0x05-user_authentication_service](https://github.com/tayloradam1999/holbertonschool-web_back_end/tree/main/0x05-user_authentication_service)
  
![](./readme_assets/4cb3c8c607afc1d1582d.jpg)
  
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
  
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes
  
<hr>
  
Here is an **example** of a Flask app that handles user authentication:
  
```python
#!/usr/bin/env python3
"""
Module used to authenticate users to database.
"""
import bcrypt
import uuid
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """
    Returns salted and hashed password using bcrypt.hashpw()
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Returns string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Hashes password with _hash_password, then saves user to database
        using self._db.add_user() and then returns the User object
        If a user already exists with the passed email, raise ValueError
        Args:
            email (str): user's email
            password (str): user's password
        Returns:
            User: User object
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound as e:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """
        Returns True if user exists and password is correct
        Args:
            email (str): user's email
            password (str): user's password
        Returns:
            bool: True if user exists and password is correct
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password)
            return False
        except NoResultFound as e:
            return False

    def create_session(self, email: str) -> str:
        """
        Finds user corresponding to email, generates new UUID,
        saves UUID to database as the user's session_id,
        then return the session_id
        Args:
            email (str): user's email
        Returns:
            str: UUID
        """
        user = self._db.find_user_by(email=email)
        session_id = _generate_uuid()
        user.session_id = session_id
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Returns corresponding User object from session_id
        Args:
            session_id (str): UUID
        Returns:
            If session ID is None, or no user found, return None
            Otherwise, return User object
        """
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound as e:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Updates corresponding user's session_id to None
        Args:
            user_id (int): user's id
        Returns:
            None
        """
        user = self._db.find_user_by(id=user_id)
        user.session_id = None

    def get_reset_password_token(self, email: str) -> str:
        """
        Finds corresponding user to email. Generates UUID
        and updates the user's <reset_token> database field.
        Then returns the reset_token
        Args:
            email (str): user's email
        Returns:
            If user does not exist, raises ValueError
            Otherwise, returns reset_token
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                reset_token = _generate_uuid()
                self._db.update_user(user.id, reset_token=reset_token)
                return reset_token
        except Exception as e:
            raise ValueError()

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Uses <reset_token> to find corresponding User.
        Hashes the password and updates the user's <hashed_password> field
        with the new hashed password and the <reset_token> field to None
        Args:
            reset_token (str): UUID
            password (str): user's password
        Returns:
            If reset_token doesn't exist, raises ValueError
            None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user:
                user.hashed_password = _hash_password(password)
                self._db.update_user(user.id, reset_token=None)
        except Exception as e:
            raise ValueError()
```