from .serializable import Serializable
from .template import Template
from .components import Component
from .exceptions import StructureError

__all__ = ("Response",)


class Response(Serializable):
    __slots__ = ("version", "template", "context", "data")

    def __init__(
        self, *components, version="2.6", quick_replies=None, context=None, data=None
    ):
        self.version = version
        if quick_replies and not components:
            raise StructureError(
                "a response template should have at least one component"
            )
        if components:
            self.template = Template(*components, quick_replies=quick_replies)
        else:
            self.template = None
        self.context = context
        self.data = data

    def to_dict(self):
        result = {"version": self.version}
        if self.template:
            result["template"] = self.template.to_dict()
        if self.context:
            result["context"] = self.context.to_dict()
        if self.data:
            result["data"] = self.data.to_dict()

        return result
