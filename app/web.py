from importlib.metadata import PackageNotFoundError, version

from flask import Flask, abort, jsonify, request

from app.calculator import add, divide

try:
    APP_VERSION = version("calc-ci-demo")
except PackageNotFoundError:
    APP_VERSION = "dev"

app = Flask(__name__)


def _two_numbers() -> tuple[float, float]:
    try:
        return float(request.args["a"]), float(request.args["b"])
    except (KeyError, ValueError):
        abort(400, description="query parameters a and b must be numbers")


@app.get("/health")
def health():
    return jsonify(status="ok", version=APP_VERSION)


@app.get("/add")
def add_endpoint():
    a, b = _two_numbers()
    return jsonify(result=add(a, b))


@app.get("/divide")
def divide_endpoint():
    a, b = _two_numbers()
    try:
        return jsonify(result=divide(a, b))
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
