# ikakao

Kakao i Open Builder SDK

Currently work in progress.

## Usage Examples

### Simple Text Response

```python
import json

from ikakao.skill import Response

r = Response("Hello, Kakao i!")
print(json.dumps(r.to_dict(), indent=2))
```

Output:
```json
{
  "version": "2.6",
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

### Multiple Text Response

```python
import json

from ikakao.skill import Response

r = Response("Hello", "Kakao", "i")
print(json.dumps(r.to_dict(), indent=2))
```

Output:
```json
{
  "version": "2.6",
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
    ]
  }
}
```
