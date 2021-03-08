from invoke import task

@task
def build(c):
    # c.run("python3.8.5 setup.py build_ext --inplace")
    c.run("python setup.py build_ext --inplace")


@task(aliases=["del"])
def delete(c):
    c.run("rm *mykmeanssp*.so")


@task
def run(c, k, n, random=True):
    # c.run("python3.8.5 setup.py build_ext --inplace")
    c.run("python setup.py build_ext --inplace")
    # c.run("python3.8.5 main.py {} {} {}".format(k, n, random))
    c.run("python main.py {} {} {}".format(k, n, random))
