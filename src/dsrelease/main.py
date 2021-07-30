import dsrelease
from invoke import Program

program = Program(version=dsrelease.__version__)
program.run()
