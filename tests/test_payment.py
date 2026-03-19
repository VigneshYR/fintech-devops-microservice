import requests

def test_payment_success():
    response = requests.post(
        "http://54.227.176.119/process-payment",
        json={"card": "1234567812345678", "amount": 100}
    )
    assert response.status_code == 200
