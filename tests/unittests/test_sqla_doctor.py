def test_add_doctor(session, faker):
    from toubib.sqla import Doctor

    doctor = Doctor(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        hiring_date=faker.date_object(),
        specialization=faker.bs(),
    )
    session.add(doctor)
    session.flush()
    assert doctor.id is not None
