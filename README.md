# Work log using a database

This terminal application is part of the **Treehouse Python Techdegree**. This application can be applied to _Start-ups_ or _SMEs_ by allowing employees to enter their name, time worked, task worked on, and general notes about the task into a database. The script registers the work tasks of a given day and allows to get access to previously registered entries. 

## Project details
* In the main menu, the user is able to choose whether to add a new entry or lookup previous entries.
* If the user chose to add a new work log, the user can register the following information in a [database](https://github.com/AaronMillOro/TH_Project4_Work_log_Database/blob/master/work_log.db) file:
```
  * User name
  * Task name
  * Number of minutes spent working on a task
  * Any additional notes
```
* If the user choose to find a previous entry, ths script propose four options: 

1. Find by **employee**
```
The user can enter the employee name and a list of employees with entries is displayed 
allowing the user to select one entry to see details.
```

2. Find by **date**
```
A list of entries with a given date is displayed and the user is able to choose one to see details.
```

3. Find by **time spent**
```
The user can enter the amount of time spent (minutes) on a task and a list of entries
containing that amount of time spent is displayed. 
The user can choose one to see details.
```

4. Find by **keyword**
```
The user can enter a keyword and a list of entries containing that keyword in task name 
or notes is displayed. The user can choose one to see details.
```

* The search logic can be found in [_tools.py_](https://github.com/AaronMillOro/TH_Project4_Work_log_Database/blob/master/tools.py)

* A 51% of the code logic is covered by tests using **coverage.py**. The results can be found [here](https://github.com/AaronMillOro/TH_Project4_Work_log_Database/tree/master/htmlcov)

To run the application type: 

>**python3 work_log_sql.py**

Enjoy! :shipit:
