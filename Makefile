INPUT=README.md
OUTPUT=README.docset

test:
	rm -rf ${OUTPUT}
	./md2dash.py ${INPUT}

install:
	pip install mistune

