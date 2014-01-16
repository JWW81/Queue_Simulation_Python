"""
-------------------------------------------------------
queue_array.py
-------------------------------------------------------
Author:  Lee Glendenning
ID:      120289190
Email:   glen9190@wlu.ca
Version: 2013-01-15
-------------------------------------------------------
"""
import copy

class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: q = Queue()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty queue.
        -------------------------------------------------------
        """
        self._values = []
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the queue.
        Use: n = len( q )
        -------------------------------------------------------
        Postconditions:
          Returns the number of values in the queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = q.is_empty()
        -------------------------------------------------------
        Postconditions:
          Returns True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: q.insert( value )
        -------------------------------------------------------
        Preconditions:
          value - a data element (?)
        Postconditions:
          value is added to the rear of the queue.
        -------------------------------------------------------
        """

        self._values.append(copy.deepcopy(value))

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = q.remove()
        -------------------------------------------------------
        Postconditions:
          Returns the value at the front of queue - the value is
          removed from queue. Returns None if queue is empty.
        -------------------------------------------------------
        """
        value = None
        if len(self._values) != 0:
            value = self._values[0]
            self._values.remove(self._values[0])
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = q.peek()
        -------------------------------------------------------
        Postconditions:
          Returns a copy of the value at the front of queue -
          the value is not removed from queue. Returns None
          if queue is empty.
        -------------------------------------------------------
        """
        if len(self._values) == 0:
            value = None
        else:
            value = copy.deepcopy(self._values[0])

        return value

    def print_i(self):
        """
        -------------------------------------------------------
        Prints the contents of queue from front to rear.
        Use: q.print_i()
        -------------------------------------------------------
        Postconditions:
          Prints each value in queue from front to rear.
          Each value starts on a new line.
        -------------------------------------------------------
        """
        for i in range(len(self._values)):
            print(self._values[i])
        return
