
import coconut


app = coconut.Coconut(
    registry_host='192.168.50.3',
    registry_port=8500,
)


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
