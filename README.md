# python-coconut
coconut python runner sdk

#### 如何安装?

`pip install -U git+https://github.com/importcjj/python-coconut.git`

#### 如何使用？

```python
import coconut

app = coconut.Coconut()

@app.register()
def add(a, b):
    """add task"""
    c = a + b
    print("{} + {} = {}".format(a, b, c))
    return c


@app.register(key="a6a099d8-dc0c-11e8-a49b-f21898282d25")
def echo(p):
    """echo task"""
    print(p)
    return p


if __name__ == '__main__':
    app.serve()

```