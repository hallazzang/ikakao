import warnings

from .serializable import Serializable
from .exceptions import UnsupportedFieldWarning

__all__ = (
    "SimpleText",
    "SimpleImage",
    "BasicCard",
    "CommerceCard",
    "ListCard",
    "Carousel",
    "to_component",
    "to_quick_reply"
)


class Component(Serializable):
    pass


class SimpleText(Component):
    __slots__ = ("text",)

    def __init__(self, *, text):
        self.text = text

    def to_dict(self):
        return {"simpleText": {"text": self.text}}


class SimpleImage(Component):
    __slots__ = ("image_url", "alt_text")

    def __init__(self, *, image_url, alt_text):
        self.image_url = image_url
        self.alt_text = alt_text

    def to_dict(self):
        return {"simpleImage": {"imageUrl": self.image_url, "altText": self.alt_text}}


class BasicCard(Component):
    __slots__ = ("title", "description", "thumbnail", "profile", "social", "buttons")

    def __init__(
        self,
        *,
        title=None,
        description=None,
        thumbnail=None,
        profile=None,
        social=None,
        buttons=None,
    ):
        self.title = title
        self.description = description
        self.thumbnail = thumbnail
        if profile:
            warnings.warn(
                "'profile' field is not supported yet", UnsupportedFieldWarning
            )
        self.profile = profile
        if social:
            warnings.warn(
                "'social' field is not supported yet", UnsupportedFieldWarning
            )
        self.social = social
        self.buttons = buttons

    def to_dict(self):
        pass


class CommerceCard(Component):
    pass


class ListCard(Component):
    pass


class Carousel(Component):
    pass


class QuickReply(Component):
    __slots__ = ("label", "action", "message_text", "block_id", "extra")

    def __init__(
        self, label, message_text, *, action="message", block_id=None, extra=None
    ):
        self.label = label
        self.message_text = message_text
        self.action = action
        self.block_id = block_id
        self.extra = extra

    def to_dict(self):
        result = {
            "label": self.label,
            "action": self.action,
            "messageText": self.message_text,
        }
        if self.action == "block" and not self.block_id:
            raise StructureError("block_id must be specified when action is 'block'")
        elif self.block_id:
            result["blockId"] = self.block_id
        if self.extra:
            result["extra"] = self.extra

        return result


def to_component(x):
    if isinstance(x, Component):
        return x
    elif isinstance(x, str):
        return SimpleText(text=x)
    else:
        raise TypeError(f"cannot convert {x} into Component")


def to_quick_reply(x):
    if isinstance(x, QuickReply):
        return x
    elif isinstance(x, str):
        return QuickReply(x, x)
    else:
        raise TypeError(f"cannot convert {x} into QuickReply")
