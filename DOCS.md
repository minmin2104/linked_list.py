<a id="linked_list"></a>

# linked\_list API Documentation

<a id="linked_list.SingularLinkedList"></a>

## SingularLinkedList Objects

```python
class SingularLinkedList()
```

<a id="linked_list.SingularLinkedList.insert_first"></a>

#### insert\_first

```python
def insert_first(value: Any)
```

Insert a node at the first index with a value of `value`.
Making it the new head of the linked list

<a id="linked_list.SingularLinkedList.insert_last"></a>

#### insert\_last

```python
def insert_last(value: Any)
```

Insert a node at the last index with a value of `value`.
Making it the new tail of the linked list

<a id="linked_list.SingularLinkedList.insert"></a>

#### insert

```python
def insert(index: int, value: Any)
```

Insert node with a value of `value` at a specific index.
If use on an index equals to the size of the linked list,
it will be the new tail.

<a id="linked_list.SingularLinkedList.index_of"></a>

#### index\_of

```python
def index_of(value: Any) -> int
```

Get the index of the first encountered node
with the value of `value` and return the index

<a id="linked_list.SingularLinkedList.first"></a>

#### first

```python
def first()
```

Get the value of the head

<a id="linked_list.SingularLinkedList.last"></a>

#### last

```python
def last()
```

Get the value of the tail

<a id="linked_list.SingularLinkedList.search"></a>

#### search

```python
def search(value: Any) -> bool
```

Return a boolean of True if
the node with a value of `value`
found within the linked list

<a id="linked_list.SingularLinkedList.delete_first"></a>

#### delete\_first

```python
def delete_first()
```

Delete the first node in the linked list

<a id="linked_list.SingularLinkedList.delete"></a>

#### delete

```python
def delete(index: int)
```

Delete the node at a specific index
in the linked list

<a id="linked_list.SingularLinkedList.update"></a>

#### update

```python
def update(index: int, value: Any)
```

Update the value of the node at index `index`
with a value of `value`

<a id="linked_list.SingularLinkedList.is_empty"></a>

#### is\_empty

```python
def is_empty() -> bool
```

Return True if the linked list is empty. False otherwise

<a id="linked_list.SingularLinkedList.size"></a>

#### size

```python
def size() -> int
```

Return the size of the linked list

