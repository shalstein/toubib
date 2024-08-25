def test_add_patient(session, faker):
    from toubib.sqla import Patient
    from datetime import datetime
    from pytest import raises
    from sqlalchemy.exc import IntegrityError

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
    patient2 = Patient(
        email=patient.email,
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        date_of_birth=datetime.strptime(faker.date(), "%Y-%m-%d"),
        sex_at_birth=faker.random_element(["FEMALE", "MALE"]),
    )
    session.add(patient2)
    with raises(IntegrityError):
        session.flush()
