#!/bin/sh
PYTHONPATH=transfer python -B -c 'import hello.greeter;hello.init();hello.greeter.greet()'
