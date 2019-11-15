# ikakao

[![shields-pypi-badge]](https://pypi.org/project/ikakao/)

[shields-pypi-badge]: https://img.shields.io/pypi/v/ikakao?style=flat-square&color=blue

Kakao i Open Builder SDK (Currently WIP)

## Roadmap

### Supported Components

- [x] SimpleText
- [x] SimpleImage
- [ ] BasicCard (Partial support)
- [ ] CommerceCard
- [ ] ListCard
- [ ] Carousel (Partial support)
- [ ] QuickReply (Partial support)

## Usage Examples

Here are some examples demonstrating various types of skill responses.

### Simple Text

```python
import json

from ikakao.skill import Response

r = Response("Hello, Kakao i!")
print(json.dumps(r.to_dict(), indent=2))
```

Output:
```json
{
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": {
          "text": "Hello, Kakao i!"
        }
      }
    ]
  }
}
```

### Multiple Text w/ Quick Reply

```python
import json

from ikakao.skill import Response

r = Response("Hello", "Kakao", "i", quick_replies="Home")
print(json.dumps(r.to_dict(), indent=2))
```

Output:
```json
{
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": {
          "text": "Hello"
        }
      },
      {
        "simpleText": {
          "text": "Kakao"
        }
      },
      {
        "simpleText": {
          "text": "i"
        }
      }
    ],
    "quickReplies": [
      {
        "label": "Home",
        "action": "message",
        "messageText": "Home"
      }
    ]
  }
}
```

### Carousel

```python
import json

from ikakao.skill import Response, BasicCard, Carousel

carousel = Carousel(
  BasicCard("Title #1", "Description"),
  BasicCard("Title #2", "Description"),
  BasicCard("Title #3", "Description"),
)
r = Response("Carousel Example", carousel, quick_replies=["Home", "Cancel"])
print(json.dumps(r.to_dict(), indent=2))
```

Output:
```json
{
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": {
          "text": "Carousel Example"
        }
      },
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "Title #1",
              "description": "Description"
            },
            {
              "title": "Title #2",
              "description": "Description"
            },
            {
              "title": "Title #3",
              "description": "Description"
            }
          ]
        }
      }
    ],
    "quickReplies": [
      {
        "label": "Home",
        "action": "message",
        "messageText": "Home"
      },
      {
        "label": "Cancel",
        "action": "message",
        "messageText": "Cancel"
      }
    ]
  }
}
```
