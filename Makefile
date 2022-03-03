.SUFFIXES:

.PHONY: default
default: _pt1.pyd

.PHONY: test
test: main.py _pt1.pyd
	python $(<)

_pt1.pyd: pt1.o pt1_wrap.o
	gcc -shared -o $(@) $(^) -lPython310 -L$(USERPROFILE)\scoop\apps\python\current\libs

pt1.o pt1_wrap.o: pt1.c pt1_wrap.c
	gcc -fPIC -c pt1.c pt1_wrap.c -I$(USERPROFILE)\scoop\apps\python\current\include

pt1_wrap.c pt1.py: pt1.swig pt1.h 
	swig -python $(<)

.PHONY: clean
clean:
	rm -rf pt1_wrap.c pt1_wrap.o pt1.o pt1.py _pt1.pyd __pycache__
