.SUFFIXES:

.PHONY: default
default: _iut.pyd

.PHONY: test
test: main.py _iut.pyd
	python $(<)

_iut.pyd: iut.o iut_wrap.o
	gcc -shared -o $(@) $(^) -lPython310 -L$(USERPROFILE)\scoop\apps\python\current\libs

iut.o iut_wrap.o: iut.c iut_wrap.c
	gcc -fPIC -c iut.c iut_wrap.c -I$(USERPROFILE)\scoop\apps\python\current\include

iut_wrap.c iut.py: iut.swig iut.h 
	swig -python $(<)

.PHONY: clean
clean:
	rm -rf iut_wrap.c iut_wrap.o iut.o iut.py _iut.pyd __pycache__
