import requests

def test_generate():
    res = requests.post("http://localhost:5000/generate", json={
        "prompt": "Write a job description for a backend engineer using Django.",
        "model": "tiiuae/falcon-7b-instruct"
    })
    assert res.status_code == 200
    print("Response:", res.json())
