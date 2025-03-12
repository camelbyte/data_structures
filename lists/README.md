Summary of basic data structures
Lists

    Ordered, mutable, allows duplicates.
    Use .append(), .remove(), .sort(), .pop(), etc.
    Iterate with for loops.


| Method            | Description                                    | Example                   |
|------------------|--------------------------------|---------------------------|
| `append(x)`      | Adds an element to the end of the list | `numbers.append(6)` |
| `extend(iterable)` | Extends list by adding multiple elements | `numbers.extend([7, 8, 9])` |
| `insert(index, x)` | Inserts an element at a specific index | `numbers.insert(2, 99)` |
| `remove(x)`      | Removes the first occurrence of `x` | `numbers.remove(3)` |
| `pop(index)`      | Removes and returns an item at `index` | `last = numbers.pop()` |
| `index(x)`       | Returns the index of `x` | `idx = numbers.index(4)` |
| `count(x)`       | Counts occurrences of `x` | `cnt = numbers.count(2)` |
| `sort()`         | Sorts the list (in-place) | `numbers.sort()` |
| `reverse()`      | Reverses the list (in-place) | `numbers.reverse()` |
| `copy()`         | Returns a shallow copy of the list | `new_list = numbers.copy()` |
| `clear()`        | Removes all elements from the list | `numbers.clear()` |



Dictionaries

    Key-value pairs, unordered, keys must be unique.
    Use .get(), .keys(), .items(), .update(), etc.
    Iterate with .items() for key-value pairs.


| Method                 | Description                                      | Example                     |
|-----------------------|--------------------------------|---------------------------|
| `keys()`              | Returns a view object of keys | `person.keys()` |
| `values()`            | Returns a view object of values | `person.values()` |
| `items()`             | Returns key-value pairs | `person.items()` |
| `get(key, default)`   | Gets a value (returns `default` if key not found) | `person.get("name")` |
| `update(dict2)`       | Merges `dict2` into current dictionary | `person.update({"age": 26})` |
| `pop(key)`            | Removes and returns a key's value | `age = person.pop("age")` |
| `popitem()`           | Removes and returns the last inserted pair | `last = person.popitem()` |
| `setdefault(key, default)` | Gets a value, or sets it if missing | `person.setdefault("gender", "Female")` |
| `copy()`              | Returns a shallow copy of the dictionary | `new_dict = person.copy()` |
| `clear()`             | Removes all key-value pairs | `person.clear()` |



Classes

    Blueprint for objects, contains attributes (data) and methods (functions).
    Use __init__() for initialization.
    Use instance methods, class methods (@classmethod), and static methods (@staticmethod).


| Feature          | Description                                  | Example |
|-----------------|----------------------------------------------|---------|
| **Instance Variable** | Specific to each instance | `self.name = name` |
| **Class Variable** | Shared across all instances | `species = "Human"` |
| **Instance Method** | Uses `self`, operates on instance data | `def greet(self):` |
| **Class Method** | Uses `@classmethod`, operates on class data | `@classmethod def set_species(cls, new_species):` |
| **Static Method** | Uses `@staticmethod`, doesn't depend on class/instance | `@staticmethod def is_adult(age): return age >= 18` |


