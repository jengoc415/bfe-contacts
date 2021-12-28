# bfe-contacts
Contacts website for BfE


1. Download files into a folder in desktop
2. Open 2 terminals
3. Might need to install Django@3.0.8 in terminal 1

Terminal 1(backend)
run these commands in the terminal
  > folder $ pipenv shell
  > $ cd contacts/
  > $ python3 manage.py makemigrations
  > $ python3 manage.py migrate
  > $ python3 manage.py runserver


Terminal 2(frontend)
run these commands in the terminal
  > $ cd frontend
  > $ npm start

http://localhost:3000/ is now up and running.
