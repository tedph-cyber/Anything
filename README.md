# Help
Welcome to the land of things, particularly for help with almost anything.

To start with we have the; 
### git command help
## Clone the Repository and Create a Feature Branch
1. Clone the repository to your local machine:
`git clone https://github.com/tedph-cyber/Anything.git
cd Anything`
2. Create a new branch for your feature:
`git checkout -b features/{your-feature-name}`

Note: Replace your-feature-name with a descriptive name for your feature. All changes must be approved by the project maintainer before merging.

3. Always update the general branch (main branch) before pulling out of it to work on a different branch
`git pull`

### Need help with merge conflict?
Contact me, TeD :)

### Tailwind CSS help
run `python manage.py tailwind start` to start the tailwind server
run `python -m pip install 'django-tailwind[reload]'` to install the tailwind package to auto reload whils coding

## Django command help
1. To download all libraries required after creating a virtual environment; run `pip install django djangorestframework django-cors-headers django-tailwind django-browser-reload django-allauth pyJWT`
2. To run the server locally: run `python manage.py runserver` then open  http://127.0.0.1:8000 after pulling