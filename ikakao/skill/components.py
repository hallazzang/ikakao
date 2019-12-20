import warnings

from .serializable import Serializable
from .exceptions import UnsupportedFieldWarning

__all__ = (
    "SimpleText",
    "SimpleImage",
    "BasicCard",
    "CommerceCard",
    "ListCard",
    "ListItem",
    "Carousel",
    "Button",
    "Link",
    "QuickReply",
)


class Component(Serializable):
    @staticmethod
    def to_component(x):
        if isinstance(x, Component):
            return x
        elif isinstance(x, str):
            return SimpleText(text=x)
        else:
            raise TypeError(f"cannot convert {x} into Component")


class SimpleText(Component):
    __slots__ = ("text",)

    def __init__(self, text):
        self.text = text

    def to_dict(self):
        return {"simpleText": {"text": self.text}}


class SimpleImage(Component):
    __slots__ = ("image_url", "alt_text")

    def __init__(self, image_url, alt_text):
        self.image_url = image_url
        self.alt_text = alt_text

    def to_dict(self):
        return {"simpleImage": {"imageUrl": self.image_url, "altText": self.alt_text}}


class BasicCard(Component):
    __slots__ = ("title", "description", "thumbnail", "profile", "social", "buttons")

    def __init__(
        self,
        title=None,
        description=None,
        *,
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
        result = {}
        if self.title:
            result["title"] = self.title
        if self.description:
            result["description"] = self.description
        if self.thumbnail:
            result["thumbnail"] = self.thumbnail.to_dict()
        if self.profile:
            result["profile"] = self.profile.to_dict()
        if self.social:
            result["social"] = self.social.to_dict()
        if self.buttons:
            result["buttons"] = [x.to_dict() for x in self.buttons]

        return {"basicCard": result}


class CommerceCard(Component):
    pass


class ListCard(Component):
    __slots__ = ("header", "items", "buttons")

    def __init__(self, header, *items, buttons=None):
        # TODO: check if items are empty
        self.header = ListItem.to_list_item(header)
        self.items = [ListItem.to_list_item(x) for x in items]
        self.buttons = [Button.to_button(x) for x in buttons]

    def to_dict(self):
        result = {
            "header": self.header.to_dict(),
            "items": [x.to_dict() for x in self.items],
        }
        if self.buttons:
            result["buttons"] = [x.to_dict() for x in self.buttons]

        return {"listCard": result}


class ListItem(Component):
    __slots__ = ("title", "description", "image_url", "link")

    def __init__(self, title, description=None, image_url=None, link=None):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.link = link and Link.to_link(link)

    def to_dict(self):
        result = {
            "title": self.title,
        }
        if self.description:
            result["description"] = self.description
        if self.image_url:
            result["imageUrl"] = self.image_url
        if self.link:
            result["link"] = self.link.to_dict()

        return result

    @staticmethod
    def to_list_item(x):
        if isinstance(x, ListItem):
            return x
        elif isinstance(x, str):
            return ListItem(x)
        else:
            raise TypeError(f"cannot convert {x} into ListItem")


class Carousel(Component):
    __slots__ = ("type", "items", "header")

    def __init__(self, *items, type="basicCard", header=None):
        # TODO: check if items are empty
        self.type = type
        self.items = items
        self.header = CarouselHeader.to_carousel_header(header)

    def to_dict(self):
        result = {
            "type": self.type,
            "items": [x.to_dict()[self.type] for x in self.items],
        }
        if self.header:
            result["header"] = self.header.to_dict()

        return {"carousel": result}


class CarouselHeader(Component):
    __slots__ = ("title", "description", "thumbnail")

    def __init__(self, title, description=None, thumbnail=None):
        self.title = title
        self.description = description
        self.thumbnail = thumbnail

    def to_dict(self):
        result = {
            "title": self.title,
        }
        if self.description:
            result["description"] = self.description
        if self.thumbnail:
            result["thumbnail"] = self.thumbnail.to_dict()

        return result

    @staticmethod
    def to_carousel_header(x):
        if isinstance(x, CarouselHeader):
            return x
        elif isinstance(x, str):
            return CarouselHeader(x)
        else:
            raise TypeError(f"cannot convert {x} into CarouselHeader")


class Button(Component):
    __slots__ = (
        "label",
        "action",
        "web_link_url",
        "os_link",
        "message_text",
        "phone_number",
        "block_id",
        "extra",
    )

    def __init__(
        self,
        label,
        action="message",
        message_text=None,
        web_link_url=None,
        os_link=None,
        phone_number=None,
        block_id=None,
        extra=None,
    ):
        # TODO: check parameters based on `action`
        self.label = label
        self.action = action
        self.message_text = message_text
        self.web_link_url = web_link_url
        self.os_link = os_link and Link.to_link(os_link)
        self.phone_number = phone_number
        self.block_id = block_id
        self.extra = extra

    def to_dict(self):
        result = {
            "label": self.label,
            "action": self.action,
        }
        if self.message_text:
            result["messageText"] = self.message_text
        if self.web_link_url:
            result["webLinkUrl"] = self.web_link_url
        if self.os_link:
            result["osLink"] = self.os_link.to_dict()
        if self.phone_number:
            result["phoneNumber"] = self.phone_number
        if self.block_id:
            result["blockId"] = self.block_id
        if self.extra:
            result["extra"] = self.extra  # TODO: transform extra

        return result

    @staticmethod
    def to_button(x):
        if isinstance(x, Button):
            return x
        elif isinstance(x, str):
            return Button(x, action="message", message_text=x)
        else:
            raise TypeError(f"cannot convert {x} into Button")


class Link(Component):
    __slots__ = ("mobile", "ios", "android", "pc", "mac", "win", "web")

    def __init__(
        self, web=None, pc=None, mobile=None, win=None, mac=None, android=None, ios=None
    ):
        # TODO: check if at least one url exists
        # I'll assume that at least `web` url is provided
        self.web = web
        self.pc = pc
        self.mobile = mobile
        self.win = win
        self.mac = mac
        self.android = android
        self.ios = ios

    def to_dict(self):
        result = {}
        if self.web:
            result["web"] = self.web
        if self.pc:
            result["pc"] = self.pc
        if self.mobile:
            result["mobile"] = self.mobile
        if self.win:
            result["win"] = self.win
        if self.mac:
            result["mac"] = self.mac
        if self.android:
            result["android"] = self.android
        if self.ios:
            result["ios"] = self.ios

        return result

    @staticmethod
    def to_link(x):
        if isinstance(x, Link):
            return x
        elif isinstance(x, str):
            return Link(x)
        else:
            raise TypeError(f"cannot convert {x} into Link")


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

    @staticmethod
    def to_quick_reply(x):
        if isinstance(x, QuickReply):
            return x
        elif isinstance(x, str):
            return QuickReply(x, x)
        else:
            raise TypeError(f"cannot convert {x} into QuickReply")
