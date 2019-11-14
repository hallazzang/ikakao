from .serializable import Serializable
from .components import to_component
from .exceptions import StructureError

__all__ = ("Template",)

MAX_COMPONENTS = 3
MAX_QUICK_REPLIES = 10


class Template(Serializable):
    __slots__ = ("components", "quick_replies")

    def __init__(self, *components, quick_replies=None):
        self.components = [to_component(x) for x in components]
        self.quick_replies = quick_replies

    def to_dict(self):
        if not self.components:
            raise StructureError("a skill template should have at least one component")

        result = {"outputs": [x.to_dict() for x in self.components]}
        if self.quick_replies:
            result["quickReplies"] = [x.to_dict() for x in self.quick_replies]

        return result
