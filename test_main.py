from fastapi.testclient import TestClient

from main import app
from payhere.core.config import settings


client = TestClient(app)
header = {}


def test_register():
    response = client.post(
        f"{settings.API_V1_STR}/register",
        json={"username": "rrrr@example.com", "password": "r"}
    )
    assert response.status_code == 200


def test_register_exist_username():
    response = client.post(
        f"{settings.API_V1_STR}/register",
        json={"username": "rrrr@example.com", "password": "r"}
    )
    assert response.status_code == 400


def test_login_wrong_password():
    response = client.post(
        f"{settings.API_V1_STR}/login",
        data={"username": "rrrr@example.com", "password": "wrong"}
    )
    assert response.status_code == 401


def test_login():
    global header
    response = client.post(
        f"{settings.API_V1_STR}/login",
        data={"username": "rrrr@example.com", "password": "r"}
    )
    header = {"Authorization": f"Bearer {response.json()['access_token']}"}
    assert response.status_code == 200


def test_accounts_create():
    response = client.post(
        f"{settings.API_V1_STR}/accounts/create",
        json={"money": 10000, "memo": "good"},
        headers=header,
    )
    assert response.status_code == 201
    response = client.post(
        f"{settings.API_V1_STR}/accounts/create",
        json={"money": 20000, "memo": "good again"},
        headers=header,
    )
    assert response.status_code == 201


def test_accounts_update():
    response = client.put(
        f"{settings.API_V1_STR}/accounts/2",
        json={"money": -10000, "memo": "bad"},
        headers=header,
    )
    assert response.status_code == 200


def test_accounts_update_wrong_id():
    response = client.put(
        f"{settings.API_V1_STR}/accounts/3",
        json={"money": -10000, "memo": "bad"},
        headers=header,
    )
    assert response.status_code == 401


def test_accounts_delete():
    response = client.delete(
        f"{settings.API_V1_STR}/accounts/2",
        headers=header,
    )
    assert response.status_code == 204


def test_accounts_delete_wrong_id():
    response = client.delete(
        f"{settings.API_V1_STR}/accounts/100",
        headers=header,
    )
    assert response.status_code == 401


def test_accounts_show():
    response = client.get(
        f"{settings.API_V1_STR}/accounts/show",
        headers=header,
    )
    assert response.status_code == 200
    assert response.json() == [{'money': 10000, 'memo': 'good'}]


def test_accounts_copy():
    response = client.post(
        f"{settings.API_V1_STR}/accounts/copy/1",
        headers=header,
    )
    assert response.status_code == 200
    assert response.json() == {'money': 10000, 'memo': 'good'}


def test_accounts_detail():
    response = client.get(
        f"{settings.API_V1_STR}/accounts/detail/1",
        headers=header,
    )
    assert response.status_code == 200
    assert response.json() == {'money': 10000, 'memo': 'good'}


def test_accounts_detail_without_token_1():
    response = client.get(
        f"{settings.API_V1_STR}/accounts/detail/1",
    )
    assert response.status_code == 401


def test_accounts_short():
    response = client.post(
        f"{settings.API_V1_STR}/accounts/short/1",
        headers=header,
    )
    assert response.status_code == 200


def test_accounts_detail_without_token_2():
    response = client.get(
        f"{settings.API_V1_STR}/accounts/detail/1",
    )
    assert response.status_code == 200
    assert response.json() == {'money': 10000, 'memo': 'good'}