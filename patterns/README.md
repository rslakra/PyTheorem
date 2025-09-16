# System Design Patterns

---

In software engineering, a system design pattern or design pattern is a general, reusable solution to a commonly 
occurring problem in many contexts in software design. A design pattern is not a rigid structure to be transplanted 
directly into source code. Rather, it is a description or a template for solving a particular type of problem that can 
be deployed in many different situations.

Design patterns can be viewed as formalized best practices that the programmer may use to solve common problems when 
designing a software application or system.

## Core Patterns

Design patterns can be organized into groups based on what kind of problem they solve.

### 1. Creational Patterns

Creational patterns create objects.


#### 1.1. Singleton Pattern

> Ensure a class has only one instance, and provide a global point of access to it.

- Use case

> This is useful for managing shared resources like a database connection or a configuration file, where only one object 
> is needed throughout the application. 

While the classic Singleton pattern is implemented differently in other languages, Python's dynamic nature offers 
several ways to achieve the same result.

##### Method 1: Using the ```__new__``` method

This is a common way to implement a **classic** singleton in Python. The ```__new__``` method is responsible for 
creating and returning a new instance of a class, and it is called before ```__init__```. By overriding this method, 
you can control the instance creation process.

> [Source Code](./creational/singleton.py)

**How it works:**
- The ```__instance``` attribute is initialized to ```None```.
- The ```__new__``` method is called every time a new ```Singleton``` object is requested.
- The method first checks if ```__instance``` is ```None```.
- If ```__instance``` is ```None```, a new instance is created using ```super().__new__(cls)``` and assigned to ```__instance```.
- In all subsequent calls, ```__instance``` will not be ```None```, so the existing instance is simply returned. 


**Pros:**
- Strictly enforces singleton behavior: No one can accidentally or intentionally create a second instance of the class by calling its constructor.
- Self-contained: The logic is encapsulated within the class itself, making it easy to see how it works. 

**Cons:**
- Multithreading issues: The basic version is not thread-safe and can lead to multiple instances being created in a multithreaded environment. This requires additional locking mechanisms to fix.
- Less "Pythonic": It involves a more traditional object-oriented pattern that is often overkill for simple cases in Python, where modules suffice. 

##### Method 2: Using a ```module``` (most Pythonic)

The simplest and most Pythonic way to achieve a singleton is to use a module. When a module is first imported, Python 
executes its code and creates a module object. Any subsequent import of that same module simply returns the existing 
module object, making it a singleton by default. 

> [Source Code](./creational/singleton_module.py)

> [Test Code](./creational/test_singleton.py)

**How it works:**
- The ```instance``` is created only once when the ```singleton_module``` module is first imported.
- Any other module that imports ```singleton_module``` will get a reference to the same ```instance``` object, ensuring a single global access point. 


**Pros:**
- Simple and readable: This is the most straightforward approach, as the intent is immediately clear.
- Encourages loose coupling: Code is not tightly coupled to a custom singleton-enforcing mechanism.
- Inherently thread-safe: In the default CPython interpreter, the module is loaded once in a single-threaded operation, so no race conditions occur during instantiation.
- Lazy initialization: The instance is only created when the module is first imported. 

**Cons:**
- Less intuitive for class-level enforcement: If you want to enforce the singleton behavior on the class itself, this method doesn't prevent other developers from creating new instances directly with MySingletonClass().

##### Method 3: Using a decorator

For more complex cases, a ```decorator``` can be used to convert any class into a singleton. The ```decorator``` wraps 
the class and manages a dictionary of instances, returning the existing one on subsequent calls.

> [Source Code](./creational/singleton_decorator.py)

**How it works:** 
- A function decorator is defined to take any class and apply the singleton pattern to it. 

Decorator (Flexible and reusable)


**Considerations for using the singleton pattern:**

- Testing: Singletons can introduce global state into an application, which can make unit testing more difficult. The state of the singleton can persist between tests, leading to dependencies and unexpected side effects.
- Global state: Singletons can behave similarly to global variables. While this provides a convenient, global access point, it can lead to tight coupling and poor design if overused.
- Multithreading: In a multithreaded environment, the classic __new__ method approach can lead to race conditions where multiple threads attempt to create an instance at the same time. This requires adding a thread-safe mechanism, such as a lock, to the implementation. 


#### 1.2. Factory Method Pattern

#### 1.3. Builder Pattern

#### 1.4. Abstract Factory Pattern

#### 1.5. Prototype Pattern



### 2. Structural Patterns

Structural patterns organize classes and objects to form larger structures that provide new functionality.

### 3. Behavioral Patterns

Behavioral patterns describe collaboration between objects.


# Reference

- [Software Design Patterns](https://en.wikipedia.org/wiki/Software_design_pattern)



# Author

---

- Rohtash Lakra
