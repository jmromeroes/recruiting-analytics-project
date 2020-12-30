import attr
import json


class ExportAttributesMixin:
    def to_dict(self):
        return attr.asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict())


class BaseEntity(ExportAttributesMixin):
    pass


class BaseValueObject(ExportAttributesMixin):
    pass
