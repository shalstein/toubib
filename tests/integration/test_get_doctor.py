from pytest import fixture


@fixture
def patient_no(faker, session):
    from toubib.sqla import Patient

    patient = Patient(
        email=faker.ascii_email(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        date_of_birth=faker.date_time,
        sex_at_birth="FEMALE",
    )
    session.add(patient)
    session.flush()
    return patient


async def test_get_doctor(client, patient_no):
    res = await client.get(f"/v1/patients/{patient_no.id}")
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["id"] == patient_no.id
    assert data["first_name"] == patient_no.first_name
    assert data["last_name"] == patient_no.last_name
    assert data["hiring_date"] == patient_no.date_of_birth.isoformat()
    assert data["sex_at_birth"] == patient_no.sex_at_birth
    assert data["email"] == patient_no.email
