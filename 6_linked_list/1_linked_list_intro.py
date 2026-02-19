#  what is linked list
#  linked list is a linear data structure where each element is a separate object
#  each element (node) of a linked list contains two parts: data and a reference (or link) to the next node in the sequence
#  linked list is a dynamic data structure which can grow and shrink at runtime by allocating and deallocating memory as needed
#  linked list can be used to implement other data structures like stacks, queues, and graphs
#  advantages of linked list over array
# 1. dynamic size: linked list can grow and shrink at runtime, while array has
# a fixed size which must be defined at the time of declaration
# 2. ease of insertion/deletion: linked list allows for easy insertion and deletion of
# elements without the need to shift elements as in an array
# 3. memory utilization: linked list can utilize memory more efficiently than an array, as
# it does not require contiguous memory allocation like an array
# 4. implementation of other data structures: linked list can be used to implement other data
# structures like stacks, queues, and graphs, while arrays may not be as efficient for these purposes

# disadvantages of linked list over array
# 1. random access: linked list does not allow for random access to elements like an
# array does, as it requires traversal from the head node to access a specific element
# 2. memory overhead: linked list requires additional memory for storing the reference to the next node, which can lead to increased memory usage compared to an array
# 3. cache locality: linked list may have poor cache locality compared to an array,
# as the nodes may not be stored in contiguous memory locations, which can lead to slower access times
# 4. complexity of operations: linked list may have higher time complexity for certain operations like
# searching for an element, as it requires traversal of the list, while an array can be accessed directly using an index
# 5. implementation complexity: linked list can be more complex to implement and manage compared to an array, as it requires handling of pointers and memory management, while arrays are simpler to use and manage in most programming languages
