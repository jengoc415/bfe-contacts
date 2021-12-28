# bfe-contacts
Contacts website for BfE


1. Download files into a folder in desktop
2. Open 2 terminals

Terminal 1(backend):
run these commands in the terminal {
  > folder$ pipenv shell
  (shell) > $ cd contacts/
  (shell) > contacts $ python3 manage.py makemigrations
  (shell) > contacts $ python3 manage.py migrate
  (shell) > contacts $ python3 manage.py runserver
}


Terminal 2(frontend):
run these commands in the terminal {
  > $ cd frontend
  > frontend $ npm start
}

http://localhost:3000/ is now up and running.
