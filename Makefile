.PHONY: all test

test:
	# TODO tests should be in tests, not src
	cd src && python -m unittest discover -v