from invenio_records_resources.services import RecordService

from oarepo_published_service.services import PublishedServiceConfig

class PublishedService(RecordService):
    def __init__(self, config: PublishedServiceConfig):
        self.config = config
