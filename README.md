# PyTheorem (Python)

---

The ```PyTheorem``` repository helps in the learning of the python language and contains the algorithms, abstract data
types and implementation of them including the
interview preparation algorithms in ```Python``` language.

[![Python Tests](https://github.com/rslakra/PyTheorem/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/rslakra/PyTheorem/actions/workflows/ci.yml)


## Folder Structure Conventions

---

Although this layout is pretty straightforward, it has several drawbacks that arise as the app complexity increases.
For example, it will be hard for you to reuse the application logic in other projects because all the functionality is
bundled in ```webapp/__init__.py```.
If you split this functionality into modules instead, then you could reuse complete modules across different projects.

```
/
├── adts                            # an adts package/
│    ├── array                      # an array package/
│    ├── graph                      # a graph package/
│    │    ├── __init__.py           # The package initializer
│    │    ├── README.md             # Instructions and helpful links
│    │    └── /                     # 
│    ├── hash                       # a hash package/
│    ├── heap                       # a heap package/
│    ├── iterator                   # an iterator package/
│    ├── lang                       # a lang package/
│    ├── linkedlist                 # a linkedlist package/
│    ├── list                       # a list package/
│    ├── logs                       # a logs package/
│    ├── map                        # a map package/
│    ├── queue                      # a queue package/
│    ├── search                     # a search package/
│    ├── security                   # a security package/
│    ├── sort                       # a sort package/
│    ├── stack                      # a stack package/
│    ├── text                       # a text package/
│    ├── time                       # a time package/
│    ├── tree                       # a tree package/
│    ├── trie                       # a trie package/
│    ├── __init__.py                # The package initializer
│    └── README.md                  # The README file of ews module
├── algos                           # an algos package/
│    ├── array                      # an array package/
│    ├── graph                      # a graph package/
│    │    ├── __init__.py           # The package initializer
│    │    ├── README.md             # Instructions and helpful links
│    │    └── _                     # The package initializer
│    ├── hash                       # a hash package/
│    ├── heap                       # a heap package/
│    ├── iterator                   # an iterator package/
│    ├── lang                       # a lang package/
│    ├── linkedlist                 # a linkedlist package/
│    ├── list                       # a list package/
│    ├── logs                       # a logs package/
│    ├── map                        # a map package/
│    ├── queue                      # a queue package/
│    ├── search                     # a search package/
│    ├── security                   # a security package/
│    ├── sort                       # a sort package/
│    ├── stack                      # a stack package/
│    ├── text                       # a text package/
│    ├── time                       # a time package/
│    ├── tree                       # a tree package/
│    ├── trie                       # a trie package/
│    ├── __init__.py                # The package initializer
│    └── README.md                  # The README file of ews module
├── aptitude                        # an aptitude package/
├── aws                             # an AWS package/
├── configs                         # The configs package
├── core                            # The core package
├── domain                          # a domain package/
├── games                           # a games package/
├── quiz                            # a quiz package/
├── README.md                       # Instructions and helpful links
├── requirements.txt                # a list of package dependencies
├── robots.txt                      # tells which URLs the search engine crawlers can access on your site
└── /                               # 
```

## Python Projects Structures

| Folder           | Description                                   |
|:-----------------|:----------------------------------------------|
| /apidoc          | the doc-generated API docs                    |
| /code            | the project files                             |
| /doc             | the documentation                             |
| /lib             | the C-language libraries                      |
| /scripts or /bin | the that kind of command-line interface stuff |
| /tests           | the tests of the project                      |


# Building Application

---

## Local Development

### Check ```Python``` settings

```shell
python3 --version
python3 -m pip --version
python3 -m ensurepip --default-pip
```

### Setup a virtual environment

```
python3 -m pip install virtualenv
python3 -m venv venv
source deactivate
source venv/bin/activate
```

## Activate ```venv```

```source``` is Linux/macOS command and doesn't work in Windows.

- Windows

```shell
venv\Scripts\activate
```

- Mac OS/Linux

```shell
source venv/bin/activate

OR

. ./venv/bin/activate  
```

Output:

```
(venv) <UserName>@<HostName> PyTheorem %
```

The parenthesized ```(venv)``` in front of the prompt indicates that you’ve successfully activated the virtual
environment.

## Deactivate Virtual Env

```shell
deactivate
```

Output:

```
<UserName>@<HostName> PyTheorem %
```

## Upgrade ```pip``` release

```shell
pip install --upgrade pip
```

## Install Packages/Requirements (Dependencies)

- Install at the system level

```shell
brew install python-requests
```

- Install in specific Virtual Env

```shell
pip install requests
pip install beautifulsoup4
python -m pip install requests
```

## Install Requirements

```shell
pip install -r requirements.txt
```

## Save Requirements (Dependencies)

```shell
pip freeze > requirements.txt
```

## Build Python Project
```shell
python -m build
```

## Configuration Setup

Set a local configuration file.
Create or update local ```.env``` configuration file.

```shell
pip install python-dotenv
cp default.env .env
```

Now, update the default local configurations as follows:

```text
# App Configs
APP_HOST = 0.0.0.0
HOST = 0.0.0.0
APP_PORT = 8080
PORT = 8080
APP_ENV = develop
DEBUG = False
#
# Pool Configs
#
DEFAULT_POOL_SIZE = 1
RDS_POOL_SIZE = 1
#
# Logger Configs
#
LOG_FILE_NAME = 'PyTheorem.log'
#
# Database Configs
#
DB_HOSTNAME = 127.0.0.1
DB_PORT =
DB_NAME = PyTheorem
DB_USERNAME = PyTheorem
DB_PASSWORD = Password
```


**By default**, Flask will run the application on **port 5000**.

## Run Flask Application

```shell
python -m flask --app webapp run --port 8080 --debug
```


**By default**, Flask runs the application on **port 5000**.

```shell
python wsgi.py

OR

#flask --app wsgi run
python -m flask --app wsgi run
# http://127.0.0.1:5000/PyTheorem

OR

python -m flask --app wsgi run --port 8080 --debug
# http://127.0.0.1:8080/PyTheorem

OR

# Production Mode

# equivalent to 'from app import app'
gunicorn wsgi:app
# gunicorn -w <n> 'wsgi:app'
gunicorn -w 2 'wsgi:app'
# http://127.0.0.1:8000/PyTheorem

gunicorn -c gunicorn.conf.py wsgi:app
# http://127.0.0.1:8080/PyTheorem

```


**Note**:- You can stop the development server by pressing ```Ctrl+C``` in your terminal.

## Access Application

```shell
- [IWS on port 8080](http://127.0.0.1:8080/PyTheorem)
- [IWS on port 8000](http://127.0.0.1:8000/PyTheorem)
- [IWS on port 5000](http://127.0.0.1:5000/PyTheorem)
```

## Testing

### Unit Tests

```shell
python -m unittest
python -m unittest discover -s ./pytheorem/tests -p "test_*.py"
```

### Performance Testing

```shell
# Run this in a separate terminal
# so that the load generation continues and you can carry on with the rest of the steps
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
```

## Capacity Planning

### CPU Bound Systems

- Formula

```text
RPS = TotalCore * (1/TaskDurationInSeconds)

i.e.:
4 * (1000/100) = 40

```

| Total Cores | Task Duration | RPS |
|:-----------:|:--------------|:----|
|      4      | 100ms         | 40  |
|      4      | 50ms          | 80  |
|      4      | 10ms          | 400 |

# Reference

## Python Basics

- [Build a Scalable Flask Web Project From Scratch](https://realpython.com/flask-project/)
- [Gunicorn - WSGI server](https://docs.gunicorn.org/en/latest/index.html)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/)
- [The Twelve Factors App](https://12factor.net/)
- [werkzeug examples](https://github.com/pallets/werkzeug/tree/main/examples)

## Logger Guide

- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)

## Documentation

- [Documentation generator and online help system](https://docs.python.org/3/library/pydoc.html)

## Load Balancing

- [Load Balancing: The Intuition Behind the Power of Two Random Choices](https://medium.com/the-intuition-project/load-balancing-the-intuition-behind-the-power-of-two-random-choices-6de2e139ac2f)
- [Load Balancing](https://go-zero.dev/en/docs/tutorials/service/governance/lb)

## Events in Distributed Systems

- [Lamport Clocks](https://sookocheff.com/post/time/lamport-clock)
- [Lamport Clocks: Determining the Order of Events in Distributed Systems](https://medium.com/outreach-prague/lamport-clocks-determining-the-order-of-events-in-distributed-systems-41a9a8489177)
- [Lamport Logical Clock](https://www.geeksforgeeks.org/lamports-logical-clock)
- [Vector Clock](https://en.wikipedia.org/wiki/Vector_clock)
- [Time in Distributed Systems Lamport Timestamps](https://www.goodmath.org/blog/2016/03/16/time-in-distributed-systems-lamport-timestamps)

## Makefile

- [6.14 Other Special Variables](https://www.gnu.org/software/make/manual/html_node/Special-Variables.html)


- [Star Wars API](https://swapi.dev/)
- [developer testing tool](https://httpbin.org/)
- [Inspect webhooks and HTTP requests](https://pipedream.com/requestbin)
- [Gunicorn Architecture](https://docs.gunicorn.org/en/latest/design.html)
- [How many concurrent requests does a single Flask process receive?](https://stackoverflow.com/questions/10938360/how-many-concurrent-requests-does-a-single-flask-process-receive?rq=4)
- [Learn FastAPI](https://fastapi.tiangolo.com/learn/)
- [Array](https://docs.python.org/3/library/array.html)

- [Beautiful Soup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start)

- [Weather-App](https://github.com/israel-dryer/Weather-App/tree/master)
- [Web-Scraping-Projects](https://github.com/israel-dryer/Web-Scraping-Projects?tab=readme-ov-file)

- [Python Projects – Beginner to Advanced](https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/)
- [The HitchHiker's Guide to Python](https://docs.python-guide.org/writing/structure/)


# Author

---

- Rohtash Lakra
