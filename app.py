from flask import Flask, render_template, request

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField


class HelloForm(FlaskForm):
    name = StringField()
    submit = SubmitField("submit")


def create_app():
    app = Flask("7guis")
    app.secret_key = "s3cr3t"

    _counter = 0

    @app.route("/hello", methods=["GET", "POST"])
    def hello():
        form = HelloForm()
        if request.method == "GET":
            return render_template("hello.html", form=form)
        else:
            return render_template("hello.html", form=form)

    @app.get("/counter")
    def counter():
        return render_template("counter.html")

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

    @app.get("/temperatures")
    def temperatures():
        return render_template("temperatures.html")

    @app.post("/celcius")
    def celcius():
        try:
            temperature_in_celcius = int(request.form.get("celcius"))
        except ValueError:
            temperature_in_celcius = 0
        temperature_in_farenheit = temperature_in_celcius * (9 / 5) + 32
        return f"""
  <input
    id="input-farenheit"
    type="number"
    hx-post="/farenheit"
    hx-target="#input-celcius"
    hx-swap="outerHTML"
    name="farenheit"
    value="{temperature_in_farenheit:.0f}"
  >
    """

    @app.post("/farenheit")
    def farenheit():
        try:
            temperature_in_farenheit = int(request.form.get("farenheit"))
        except ValueError:
            temperature_in_farenheit = 0
        temperature_in_celcius = (temperature_in_farenheit - 32) * (5 / 9)
        return f"""
  <input
    id="input-celcius"
    type="number"
    hx-post="/celcius"
    hx-target="#input-farenheit"
    hx-swap="outerHTML"
    name="celcius"
    value="{temperature_in_celcius:.0f}"
  >
    """

    return app
