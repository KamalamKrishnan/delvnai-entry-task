# Part A – Fundamentals

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

4.*The reasons could be*

1.Slower reponse time ( High Latency )

2.Multiple users ( high traffic ) using the the service at the same time than the server can handle ( IRCTC ticket booking scenarios )
Slower response time can be checked in the design of the application by reducing the number of users to see how much the app can handle as these are related to the non-functional requirements of an application design

The above two are from the server side, but network issues could also be there from the client side.

# Part B – Coding

## Files

- `transaction_summary.py` – Python program
- `transactions.csv` – Sample transaction data

## How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run the command:

```bash
python transaction_summary.py
```

## What the Program Does

- Reads transaction data from a CSV file.
- Calculates the total amount for each category.
- Displays the totals sorted from highest to lowest.

## Error Handling

The program uses `try-except` blocks to handle errors gracefully.

- If `transactions.csv` is not found, it displays an error message.
- If a row contains an invalid amount or a missing field, that row is skipped and the remaining data is processed without stopping the program.

## One Thing I Would Improve

If I had more time, I would allow the user to provide the CSV file name as input and display the output in a more formatted table. Also, would have created a better sample file with different types of errors to handle

# Part C

The part A questions didn't seem any difficult to me, process, thread, join and commit concepts are the theoretical ones which I am good at and even relating all those to real life examples too ( as I understand them )

For part B, I know what to do, how to read a csv file, and how to sort them using sorted() but the try-except blocks to handle errors was the suggestion I got from gpt as I was unsure about whether to use numpy error handlings like dropna, fillna ( bfill, ffill ),etc or not, then I got to know from gpt that why not to use pandas - csv is a built-in module in python unlike pandas which is a dataframe structure and henceforth its methods cant be used, and also it is not mentioned to clean the code as we don't know what should be the value there, but just to handle the error.

key=lambda item: item[1], --- this line of code is also new to me, which I understood later as 

If we simply wrote: sorted(category_totals.items()) then Python would sort alphabetically:
Books
Food
Shopping
Software
Travel

But we want:
Software 4199
Travel 3500
Food 750
Shopping 650
Books 450
