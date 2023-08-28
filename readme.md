1. install python (3.9.5)
2. create virtual environment 
python3 -m venv venv
3. activate virtual envinronment
source venv/bin/activate
4. install python dependencies
pip install -r requirements.txt
5. crate  & apply migrations
python manage.py makemigrations | python manage.py migrate
6. add crontab 
python3 manage.py crontab add
7. verify crontab added or not 
crontab -l