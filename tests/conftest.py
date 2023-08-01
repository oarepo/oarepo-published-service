import pytest
from invenio_app.factory import create_api as _create_api


@pytest.fixture(scope="module")
def app_config(app_config):
    from oarepo_published_service.services import (
        PublishedService,
        PublishedServiceConfig,
    )

    app_config["OAREPO_PUBLISHED_SERVICE"] = PublishedService
    app_config["OAREPO_PUBLISHED_SERVICE_CONFIG"] = PublishedServiceConfig

    return app_config


@pytest.fixture(scope="module")
def create_app(instance_path, entry_points):
    """Application factory fixture."""
    return _create_api


@pytest.fixture(scope="module")
def published_service(app):
    from oarepo_published_service.proxies import current_service

    return current_service


@pytest.fixture(scope="session", autouse=True)
def faker_session_locale():
    return ["cs_CZ"]


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return 42


@pytest.fixture
def sample_record(faker):
    return {
        "metadata": {
            "title": faker.text(max_nb_chars=20),
            "status": faker.word(ext_word_list=["ok", "skipped"]),
        }
    }
