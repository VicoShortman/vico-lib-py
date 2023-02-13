import sys


def dict_merge(dict1: dict, dict2: dict) -> dict:
    """
    Merges two dicts to one and returns it. Dose not manipulate the given dicts.
    The second dict will be the added one. If there are duplicate keys, the value will be taken from the second dict!
    :params dict1 First Dict
    :params dict2 Second Dict
    :return merged dict
    """
    # check if py version supports merging operator ('|')
    supports_merge = sys.version_info >= (3, 9)
    if supports_merge:
        return dict1 | dict2
    else:
        return {**dict1, **dict2}
