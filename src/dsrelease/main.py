import dsrelease
from dsrelease import tasks
from invoke import Collection, Program

program = Program(
    namespace=Collection.from_module(tasks), version=dsrelease.__version__
)
program.run()
