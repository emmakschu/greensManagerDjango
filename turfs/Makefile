CC = gcc
CFLAGS = `python-config --cflags` -c -fPIC
LD = `python-config --ldflags` -shared

CY = cython
CYFLAGS = -3

views_cython: cython/viewsCython.pyx
	$(CY) $(CYFLAGS) -o cython/viewsCython.c \
		cython/viewsCython.pyx

views_build: views_cython
	$(CC) $(CFLAGS) -o cython/viewsCython.o \
		cython/viewsCython.c

views_link: views_build
	$(CC) $(LD) -o cython/viewsCython.so cython/viewsCython.o
