PYTHON=python

.PHONY:
	clean
	install
	run
	test
	report
	partial-report

.DEFAULT_GOAL: test


install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	coverage run -m unittest

run:
	$(PYTHON) -m src.pyman

clean:
	fdfind -I cache . -x rm -rf

report:
	coverage html

partial-report:
	coverage html --skip-covered
