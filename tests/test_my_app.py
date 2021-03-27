import json


def test_hello_world(app, client):
    res = client.get('/')
    mimetype = 'text/html; charset=utf-8'
    assert res.status_code == 200
    assert res.content_type == mimetype
    assert res.get_data(as_text=True) == '<p>Hello, World</p>'


def test_hello_world_json(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    res = client.post('/', headers=headers)
    assert res.status_code == 200
    assert res.content_type == mimetype
    exp = {'message': 'Hello, World'}
    assert exp == json.loads(res.get_data(as_text=True))

