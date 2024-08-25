def test_add_patient(session, faker):
    from datetime import datetime

    from toubib.sqla import Patient

    patient = Patient(
        email=faker.ascii_email(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        date_of_birth=datetime.strptime(faker.date(), "%Y-%m-%d"),
        sex_at_birth=faker.random_element(["FEMALE", "MALE"]),
    )
    session.add(patient)
    session.flush()
    assert patient.id is not None
