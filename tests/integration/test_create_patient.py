async def test_create_patient(client, faker):
    body = {
        "email": faker.ascii_email(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "date_of_birth": faker.date(),
        "sex_at_birth": "FEMALE",
    }
    res = await client.post("/v1/patients", json=body)
    assert res.status_code == 201
    data = res.json()["data"]
    assert data["id"] is not None
    assert data["first_name"] == body["first_name"]
    assert data["last_name"] == body["last_name"]
    assert data["email"] == body["email"]
    assert data["date_of_birth"] == body["date_of_birth"]
    assert data["sex_at_birth"] == body["sex_at_birth"]
