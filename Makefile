init:
	pip3 install -r requirements.txt

test:
	pytest tests/

run:
	python3 main.py