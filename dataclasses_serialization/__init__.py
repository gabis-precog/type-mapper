"""

Suppose we have the following dataclass:

>>> from dataclasses import dataclass
>>> @dataclass
... class InventoryItem:
...    name: str
...    unit_price: float
...    quantity_on_hand: int

Then we may serialize/deserialize it to/from JSON by using `dataclasses_serialization.mapper.json_mapper.JsonMapper`

>>> from dataclasses_serialization.mapper.json_mapper import JsonMapper
>>> mapper = JsonMapper()

This can be used to serialize:

>>> mapper.serialize(InventoryItem("Apple", 0.2, 20))
{'name': 'Apple', 'unit_price': 0.2, 'quantity_on_hand': 20}

and deserialize:

>>> mapper.deserialize(InventoryItem, {'name': 'Apple', 'unit_price': 0.2, 'quantity_on_hand': 20})
InventoryItem(name='Apple', unit_price=0.2, quantity_on_hand=20)


"""

__version__ = "1.4.0"
