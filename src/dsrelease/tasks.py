from invoke import task


@task
def tag(c):
    """
    Tags a new git release, automates merging develop into master.
    Follows semantic versioning.
    """
    print("it works!")
    pass
