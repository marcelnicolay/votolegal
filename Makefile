.SILENT:

all:

clean:
	find . -iname '*.pyc' | xargs rm -f

db:
	PYTHONPATH=`pwd` python voto_legal/manage.py syncdb
	PYTHONPATH=`pwd` python voto_legal/manage.py migrate

start:
	PYTHONPATH=`pwd` python voto_legal/manage.py runserver 0.0.0.0:8000