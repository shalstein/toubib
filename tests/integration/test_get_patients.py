from datetime import datetime

from pytest import fixture


@fixture
def sorted_patient_ids(faker, session):
    from toubib.sqla import Patient

    patients = []
    for i in range(15):
        patient = Patient(
            email=faker.ascii_email(),
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            date_of_birth=datetime.strptime(faker.date(), "%Y-%m-%d"),
            sex_at_birth=faker.random_element(["FEMALE", "MALE"]),
        )
        session.add(patient)
        patients.append(patient)

    session.flush()

    return [
        patient.id
        for patient in sorted(patients, key=lambda patient: patient.last_name.lower())
    ]


async def test_get_patients(client, sorted_patient_ids):
    res = await client.get("/v1/patients")
    assert res.status_code == 200
    data = res.json()["data"]

    assert [patient["id"] for patient in data] == sorted_patient_ids[
        :10
    ], f"Expected first 10 sorted patient IDs {sorted_patient_ids[:10]}, but got {[patient['id'] for patient in data]}"
