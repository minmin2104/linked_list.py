# Linked List Python Module

A minimalist python linked list module. It provides **Singular Linked List**
module only. At least for now. More to come for Doubly and Circular.

## Installing

**Recommended way**

```
python -m venv .venv
source .venv/bin/activate
pip install git+https://github.com/minmin2104/linked_list.py.git
```

## Example usage
```py
from linked_list import SingularLinkedList


if __name__ == "__main__":
    ll = SingularLinkedList()

    ll.insert_first(10)
    ll.insert_last(30)
    ll.insert(1, 20)
    ll.insert_last(40)
    ll.delete(1)
    print(ll.search(40))
    print(ll)
```
