from flask_principal import Identity
from invenio_access.permissions import any_user, system_identity
from invenio_app.factory import create_api as _create_api
import pytest

from model.services.records.config import ModelServiceConfig
from oarepo_published_service.services import (
    PublishedService,
    PublishedServiceConfig
)

@pytest.fixture(scope="module")
def app_config(app_config):
    app_config[
        "RECORDS_REFRESOLVER_CLS"
    ] = "invenio_records.resolver.InvenioRefResolver"
    app_config[
        "RECORDS_REFRESOLVER_STORE"
    ] = "invenio_jsonschemas.proxies.current_refresolver_store"
    
    app_config["OAREPO_PUBLISHED_SERVICE"] = PublishedService
    app_config["OAREPO_PUBLISHED_SERVICE_CONFIG"] = PublishedServiceConfig

    return app_config


@pytest.fixture(scope="module")
def create_app(instance_path, entry_points):
    """Application factory fixture."""
    return _create_api

@pytest.fixture(scope="module")
def published_service(app):
    return PublishedService(
        config=PublishedServiceConfig(
            proxied_drafts_config=ModelServiceConfig()
        )
    )


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
            "title": faker.word(),
            "status": faker.word(ext_word_list=["ok", "skipped"]),
        }
    }