from invenio_drafts_resources.services.records import RecordServiceConfig
from oarepo_runtime.config.permissions_presets import OaiHarvesterPermissionPolicy


class PublishedServiceConfig:
    permission_policy_cls = OaiHarvesterPermissionPolicy

    def __init__(self):
        self._drafts_config = RecordServiceConfig()

    def __getattr__(self, name):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            return getattr(self._drafts_config, name)
