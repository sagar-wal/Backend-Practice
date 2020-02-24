# Notes_Creator
NoteZ- A notes-creating app in Django
 
## Steps to Reproduce
* Start off by forking this repository and cloning it to get your local copy. Make sure you run this in git bash.

  ```bash
  $ git clone https://github.com/sagar-wal/Notes_Creator.git
  ```
* If you prefer a virtual-environment (venv) you should have pip and venv installed.

  ```bash
  $ sudo apt install python3-pip python3-dev
  $ sudo apt-get install python3-venv
  ```
 
* Initiate a python 3 environment.
  
  ```bash
  $ python3 -m venv env 
  ```
* Activate your virtual environment.
  
  ```bash
  $ source env/bin/activate
  ```
  
  After successful activation, the code within parentheses will appear before the prompt in the bash similar to this:
  ```bash
  (env) <directory>$ 
  ``` 
  You can watch this video on how to install venv : <a href="https://www.youtube.com/watch?v=mqlCk_WCK2E">https://www.youtube.com/watch?v=mqlCk_WCK2E</a>
  
  The source code is contained in the 'note_creator' directory. Open that directory before running the forthcoming commands.
 * Initialise the database
   
   ```bash
   $ python manage.py makemigrations
   $ python manage.py migrate
   ```
 
 * All set ! Now run the server and get started !
   
* Run the following command in your terminal.

  ```bash
  $ python manage.py runserver
  ```
  
* Navigate to http://localhost:8000 in any web browser to see it in action.Have fun!
