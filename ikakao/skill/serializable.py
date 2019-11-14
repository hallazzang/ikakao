from ..utils import compact_json


class Serializable:
    def __repr__(self):
        return compact_json(self.to_dict())

    def to_dict(self):
        raise NotImplementedError
