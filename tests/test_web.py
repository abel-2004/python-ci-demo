from app.web import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_health_reports_ok():
    response = client().get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_add_endpoint_returns_sum():
    response = client().get("/add?a=2&b=3")

    assert response.get_json() == {"result": 5.0}


def test_divide_endpoint_returns_quotient():
    response = client().get("/divide?a=10&b=4")

    assert response.get_json()["result"] == 2.5


def test_divide_by_zero_returns_400():
    assert client().get("/divide?a=1&b=0").status_code == 400


def test_non_numeric_input_returns_400():
    assert client().get("/add?a=x&b=3").status_code == 400
