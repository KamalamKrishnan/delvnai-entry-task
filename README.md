1.*Difference between a Process and a Thread*
    A process is an independent program running on a computer with its own memory and resources. A thread is a smaller unit of execution inside a process, and multiple threads can share the same memory.
    Example: process can be imagined as a restaurant while threads are its various delivery applications like swiggy, zomato,etc

2.*Difference between LEFT JOIN and INNER JOIN*
    An inner join is like intersection of two tables, returning only the matching values whereas a left join returns all the values from left table irrespective of intersecting or not.

| Student_ID | Name    |
|------------|---------|
| 1          | Alice   |
| 2          | Bob     |
| 3          | Charlie |

| Student_ID | Marks |
|------------|-------|
| 1          | 90    |
| 2          | 80    |

Inner join result:
| Name  | Marks |
|-------|-------|
| Alice | 90    |
| Bob   | 80    |

Left join result:
| Name    | Marks |
|---------|-------|
| Alice   | 90    |
| Bob     | 80    |
| Charlie | NULL  |

3.*What is Version Control?*

Version control is a system that keeps track of changes made to code. It allows developers to go back to previous versions if something goes wrong and makes it easier for multiple people to work on the same project.

A commit is like saving a checkpoint of our work with a message explaining what you changed like a note in the diary.

A pull request is a request asking others to review our changes before they are added to the main project.

4.The reasons could be:
    1.Slower reponse time ( low Latency )
    2.Multiple users using the the service at the same time than the server can handle ( IRCTC ticket booking scenarios )
    Slower response time can be checked in the design of the application by reducing the number of users to see how much the app can handle as these are related to the non-functional requirements of an application design
    The above two are from the server side, but network issues could also be there from the client side.