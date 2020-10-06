.PHONY: all test

test:
	cd src && python -m unittest discover -v