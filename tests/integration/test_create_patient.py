from pytest import mark


def patient_body(faker):
    return {
        "email": faker.ascii_email(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "date_of_birth": faker.date(),
        "sex_at_birth": faker.random_element(["FEMALE", "MALE"]),
    }


@mark.filterwarnings("ignore:transaction already deassociated from connection")
async def test_create_patient(client, faker):
    body1 = patient_body(faker)
    body2 = patient_body(faker)
    body2["email"] = body1["email"]

    res = await client.post("/v1/patients", json=body1)
    assert res.status_code == 201
    data = res.json()["data"]
    assert data["id"] is not None
    assert data["first_name"] == body1["first_name"]
    assert data["last_name"] == body1["last_name"]
    assert data["email"] == body1["email"]
    assert data["date_of_birth"] == body1["date_of_birth"]
    assert data["sex_at_birth"] == body1["sex_at_birth"]

    res = await client.post("/v1/patients", json=body2)
    assert res.status_code == 400
