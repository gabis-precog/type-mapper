from typing import Dict

from dataclasses_serialization.mapper.typing import SerializerMap


def merge_lazy_dicts(mapper,
                     *dicts: SerializerMap
                     ) -> Dict:
    resolved_dicts = {}
    for single_dict in dicts:

        if callable(single_dict):
            single_dict = single_dict(mapper)

        if single_dict is None:
            single_dict = {}

        resolved_dicts = {**resolved_dicts, **single_dict}

    return resolved_dicts


def any_class_deserializer(deserializer):
    def wrapped(cls, *args):
        return deserializer(*args)

    return wrapped
