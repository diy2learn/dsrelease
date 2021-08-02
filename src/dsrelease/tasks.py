from invoke import task


@task
def tag(ctx):
    """
    Tags a new git release, automates merging develop into master.
    Follows semantic versioning.
    """
    current_ver = ctx.run("git describe --tags --abbrev=0", hide=True, warn=True).stdout
    return current_ver


@task
def update_tag(ctx):
    current_ver = tag(ctx)
    ver_major, ver_minor, ver_patch = current_ver.split(".")[:3]
    ver_patch = int(ver_patch) + 1
    update_ver = f"{ver_major}.{ver_minor}.{ver_patch}"
    print("current_ver: ", current_ver)
    print("update_ver: ", update_ver)
    return update_ver


@task
def release_start(ctx):
    update_ver = update_tag(ctx)
    ctx.run(f"git flow start {update_ver}")
