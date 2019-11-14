import json


def compact_json(x):
    return json.dumps(x, separators=(",", ":"))
