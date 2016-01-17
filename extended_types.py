from schematics.types import BaseType
from enum import Enum

class EnumType(BaseType):

    def __init__(self, enum_meta, *args, **kwargs):

        if not isinstance(enum_meta, EnumMeta):
            raise TypeError('"enum_object" must be an EnumMeta type <Package: enum34>')

        super(EnumType, self).__init__(
            choices=[k for k, _ in enum_meta.__members__.items()],
            *args,
            **kwargs
        )

    def to_primitive(self, value, context=None):
        return value.value
