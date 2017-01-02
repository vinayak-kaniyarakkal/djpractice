init:
	pip install -r requirements.txt

clean:
	find . -name '*~' -delete
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete

server:
	python djpractice/manage.py runserver

shell:
	python djpractice/manage.py shell

migrate:
	python djpractice/manage.py makemigrations && python djpractice/manage.py migrate
