PYTHON=$[python]
TEST_RUNNER=coverage run

.PHONY:
	clean
	install
	run
	test

.DEFAULT_GOAL: test


install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(TEST_RUNNER) -m unittest

run:
	$(PYTHON) -m src

clean:
	fdfind -I cache . -x rm -rf
