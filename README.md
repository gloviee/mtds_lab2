# mtds_lab2

# Character List Manager — Data Structures Lab

This application implements a **character list** data structure, which can operate in two variants:
1. **Based on a built-in array (`list`)** — `ArrayList` implementation
2. **Singly linked circular list** — `LinkedCircularList` implementation

Each variant implements a full set of methods for list element manipulation: adding, deleting, inserting, searching, cloning, reversing, expanding with other lists, and more.

---

## 🛠 Implemented Methods

The `ArrayList` class implements the following methods:

- `length()` — list length
- `append(element)` — add a character to the end
- `insert(element, index)` — insert at any position
- `delete(index)` — delete an element by index
- `deleteAll(element)` — delete all occurrences of a character
- `get(index)` — get an element by position
- `clone()` — clone the list
- `reverse()` — reverse the list
- `findFirst(element)` — find the first occurrence
- `findLast(element)` — find the last occurrence
- `clear()` — clear the list
- `extend(otherList)` — extend the list with another (copied, not passed by reference)

---

## 🚀 How to Clone the Repository and Run

### 1. Clone the Repository

```cmd
git clone https://github.com/gloviee/mtds_lab2.git
cd mtds_lab2
```

### 2. Run demo
```cmd 
python main.py
```


### 3. Run unit test
```cmd
python -m unittest discover
```

### Failed unit test commit 

- Tap [here](https://github.com/gloviee/mtds_lab2/commit/cf1f08fd66a40173ade7f5628471753340eb76a0)