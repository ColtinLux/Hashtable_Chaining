# Hashtable_Chaining
Chaining Example

lux.coltin@gmail.com

More Info: http://failuresofatwentysomething.com/hashtable-chaining/

Date: 11/27/2018

Project: Create a Hash Table (Chaining) example. 

Project Description: Chaining is a common solution to Hash Table collisions, which involves the use of linked lists. What is a hash table? What is a hash table collision?

Program Description: Written in Python, this program (hashtable_chaining_c.py) utilizes two existing parent classes (hashtable_c.py and linkedlist_c.py). We create a sub-class ‘chained_hashtable’ which inherits the hashtable class. This sub-class will replace the rehash function by creating a linked list in the event of a collision. I added search and print functions into the program’s functionality as well. We could also add a delete function (among others) if needed.  

Failure: Turns out hash tables are very fast! On average, search, insertion, and deletion are Big O(1). The use of hash tables can significantly cut your runtime down. By utilizing a data structure such as a hash table in my current project, I now have a more efficient algorithm. 

Result: In creating the Linked List class and Hash Table parent class for use in the Hash Table – Chaining sub-class, we now also have access to deploy the use of these in other programs in the future.
