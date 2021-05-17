TESTS := $(wildcard test/test_*.py)
PYFILES := $(wildcard defect_detection/*.py)

doc: FORCE
	sphinx-build -M html doc/source doc/build
	#sphinx-build -M latexpdf doc/source doc/build
	

test: FORCE
	pytest --ignore=sandbox/ --cov=./ --cov-report=html --cov-config=.coveragerc | tee doc/source/_static/doc_test.txt

lint: FORCE
	pylint $(PYFILES) | tee todos.md

FORCE:

