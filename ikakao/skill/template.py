from .serializable import Serializable
from .components import QuickReply, to_component, to_quick_reply
from .exceptions import StructureError

__all__ = ("Template",)

MAX_COMPONENTS = 3
MAX_QUICK_REPLIES = 10


class Template(Serializable):
    __slots__ = ("components", "quick_replies")

    def __init__(self, *components, quick_replies=None):
        self.components = [to_component(x) for x in components]
        if quick_replies:
            if isinstance(quick_replies, (tuple, list)):
                self.quick_replies = [to_quick_reply(x) for x in quick_replies]
            elif isinstance(quick_replies, QuickReply):
                self.quick_replies = [quick_replies]
            elif isinstance(quick_replies, str):
                self.quick_replies = [to_quick_reply(quick_replies)]
            else:
                raise StructureError(f"cannot assign {quick_replies} to quick_replies")
        else:
            self.quick_replies = None

    def to_dict(self):
        if not self.components:
            raise StructureError("a skill template should have at least one component")

        result = {"outputs": [x.to_dict() for x in self.components]}
        if self.quick_replies:
            result["quickReplies"] = [x.to_dict() for x in self.quick_replies]

        return result
