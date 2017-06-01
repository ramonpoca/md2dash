INPUT=README.md
OUTPUT=README.docset

test:
	rm -rf ${OUTPUT}
	./md2dash ${INPUT}

install:
	pip install mistune

