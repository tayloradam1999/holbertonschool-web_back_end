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