from invenio_records_resources.services import RecordService


class PublishedService(RecordService):
    def __init__(self, config):
        self.config = config
