from fastapi.testclient import TestClient
from app import app

client = TestClient(app=app)
def test_websocket():
    token = ""
    headers = {"Authorization": f"Bearer {token}"}
    with client.websocket_connect("/ws", headers=headers) as websocket:
        websocket.send_text("hello , server")
        response = websocket.receive_text()
test_websocket()

