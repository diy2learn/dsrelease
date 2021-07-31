from invoke import task


@task
def tag(ctx):
    """
    Tags a new git release, automates merging develop into master.
    Follows semantic versioning.
    """
    current_ver = ctx.run("git describe --tags --abbrev=0", hide=True, warn=True).stdout
    print("current_ver: ", current_ver)
