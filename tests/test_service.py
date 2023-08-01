from invenio_access.permissions import system_identity


def test_create(published_service, sample_record):
    res = published_service.create(system_identity, sample_record)

    print(res)
