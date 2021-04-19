from invoke import task


@task
def build(c):
    # Linux
    c.run("python3.8.5 setup.py build_ext --inplace")
    # Windows
    # c.run("python setup.py build_ext --inplace")


@task(aliases=["del"])
def delete(c):
    c.run("rm *mykmeanssp*.so")


# command: python3.8.5 -m invoke run -k -n --[ no-] Random
# to run without random --no-Random
@task
def run(c, k=None, n=None, Random=True):
    build(c)
    if Random:
        # Linux
        c.run("python3.8.5 main.py 0 0 True")
        # Windows
        # c.run("python main.py 0 0 True")
    else:
        # Linux
        c.run("python3.8.5 main.py {} {} 0".format(k, n))
        # Windows
        # c.run("python main.py {} {} False".format(k, n))
