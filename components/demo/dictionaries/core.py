"""
Dictionary helper functions

The pick and omit functions are similar to select-keys and dissoc in Clojure,
and I have borrowed the naming from the JavaScript equivalents in the Lodash.js library.

"""


def pick(data: dict, keys: set) -> dict:
    return {k: v for k, v in data.items() if k in keys}


def omit(data: dict, keys: set) -> dict:
    return {k: v for k, v in data.items() if k not in keys}
