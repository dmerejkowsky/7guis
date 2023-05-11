from flask import Flask, render_template


def create_app():
    app = Flask("counter")

    _counter = 0

    @app.get("/")
    def home():
        return "hello"

    @app.get("/counter")
    def counter():
        return render_template("counter.html", counter=_counter)

    @app.post("/up")
    def on_up():
        nonlocal _counter
        _counter += 1
        return str(_counter)

    @app.post("/down")
    def on_down():
        nonlocal _counter
        _counter -= 1
        return str(_counter)

    return app
