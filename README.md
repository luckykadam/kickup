# kickup
Kickup: Template for Quick Projects (Machine Coding Interviews)

## About
This repo serves as a great starting point for fast prototype projects.
* Specially useful in Machine Coding interviews, when time is limited (~1 hour) and you can't afford to waste time on boiler plate code.
* Implementation of Data Access Layer (csv) and Command Line Interface is provided, which are essential components of a demoable project.
* Compelte code is under 200 line of code, which makes it easy to understand and extend.

## Design
The code is designed as three modules.
1. Command line interface: The module responsible for interaction with the end-user. It can be replaced with any kind of interface without affecting other module. For example: it can be replaced by REST API.
2. Business Logic: This module contains the core logic of the application.
3. Data Access Object: This module is responsible for interacting with the storage and provide the data to the application. Currently it reads from csv file, and keeps the data in memory. It can easily be replaced with another DAO which interacts with Database.


## Implementation
Implementation is done in python3.6. No external library is used.
<br> Although it implements Group Management System, this code can be used as a started code for any quick project.

### Files
All the source code is inside `src` directory.

* **command_line_interface.py**
This file represents Command Line Interface module. It interacts directly with `GroupManager`, but not with data access module.
<br> It extends [Cmd](https://docs.python.org/3/library/cmd.html#cmd.Cmd) class, and can be started by `cmdloop` function.

* **group_manager.py**
This file represents Group Management module. It interacts directly with data access module.
It provides functions: `check_user_in_group`, `add_user_to_group` and `remove_user_from_group`.

* **csv_dao.py**
This file represents CSV Data Access Object module. It interacts with storage(csv files) to provide data access to other modules.

* **models.py**
This file contains the definition of entities.

* **main.py**
This file stitch together all the module into an application.

* **exceptions.py**
This file contains definition of commonly occurring exceptions.

## Usage/Execution
The application can be started using command
```
cd src
python src/main.py
```
The program load the data from data directory and provides a command prompt for basic functionality.
### Commands
1. `help`: To know about available commands.
2. `users`: To see all users.
3. `groups`: To see all groups.
4. `assign <user_id> <group_id>`: To assign a user to a group.
5. `remove <user_id> <group_id>`: To remove a user from a group.
6. `exit`: To exit from command prompt.
