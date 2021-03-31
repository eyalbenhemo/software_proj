from invoke import task


@task
def build(c):
    # c.run("python3.8.5 setup.py build_ext --inplace")
    c.run("python setup.py build_ext --inplace")


@task(aliases=["del"])
def delete(c):
    c.run("rm *mykmeanssp*.so")


# command: python3.8.5 -m invoke run -k -n --[ no-] Random
# to run without random --no-Random
@task
def run(c, k, n, Random=True):
    # c.run("python3.8.5 setup.py build_ext --inplace")
    c.run("python setup.py build_ext --inplace")
    # c.run("python3.8.5 main.py {} {} {}".format(k, n, random))
    c.run("python main.py {} {} {}".format(k, n, Random))
