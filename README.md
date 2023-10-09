# AirBnB Clone Project - The Console

![AirBnB Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/1280px-Airbnb_Logo_B%C3%A9lo.svg.png)

## Description of the Project

This project is the first step in building a full web application that emulates the core functionalities of the popular platform Airbnb. This initial step focuses on creating a command-line interpreter (CLI) to manage AirBnB objects. The project sets the foundation for subsequent development tasks, including HTML/CSS templating, database storage, API integration, and front-end development.

## Description of the Command Interpreter

The command interpreter, implemented in `console.py`, serves as a tool to interact with and manage AirBnB objects. It allows users to perform various operations on objects, such as creating, retrieving, updating, and deleting them. The interpreter follows a Shell-like interface and provides commands to manipulate AirBnB objects.

## How to Start It

To start the AirBnB Clone command interpreter, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/AirBnB_clone.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AirBnB_clone
   ```

3. Run the command interpreter:

   ```bash
   ./console.py
   ```

## How to Use It

Once you have started the command interpreter, you can use the following commands to manage AirBnB objects:

- `create`: Create a new AirBnB object (e.g., User, State, City, Place).
  Example:
  ```bash
  (hbnb) create User
  ```

- `show`: Retrieve information about a specific object by specifying its class name and ID.
  Example:
  ```bash
  (hbnb) show User 1234-5678-9012
  ```

- `all`: List all objects of a given class or list all objects if no class is specified.
  Example:
  ```bash
  (hbnb) all
  (hbnb) all State
  ```

- `update`: Update attributes of an object by specifying its class name, ID, attribute name, and attribute value.
  Example:
  ```bash
  (hbnb) update User 1234-5678-9012 first_name "John"
  ```

- `destroy`: Delete an object by specifying its class name and ID.
  Example:
  ```bash
  (hbnb) destroy Place 9876-5432-1098
  ```

- `quit` or `EOF`: Exit the command interpreter.
  Example:
  ```bash
  (hbnb) quit
  ```

- `help`: Display a list of available commands or get help for a specific command.
  Example:
  ```bash
  (hbnb) help
  (hbnb) help show
  ```

## Examples

Here are some examples of how to use the AirBnB Clone command interpreter:

1. Creating a new User object:
   ```bash
   (hbnb) create User
   ```

2. Listing all City objects:
   ```bash
   (hbnb) all City
   ```

3. Updating the name attribute of a Place object:
   ```bash
   (hbnb) update Place 1234-5678-9012 name "Cozy Cabin"
   ```

4. Deleting a State object:
   ```bash
   (hbnb) destroy State 9876-5432-1098
   ```

5. Exiting the command interpreter:
   ```bash
   (hbnb) quit
   ```

The AirBnB Clone command interpreter provides a convenient way to manage and manipulate AirBnB objects, making it an essential tool for developing the full-fledged AirBnB clone web application.
