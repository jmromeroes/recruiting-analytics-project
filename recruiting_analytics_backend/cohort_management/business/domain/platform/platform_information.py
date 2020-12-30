import attr
from typing import List

from ..base import BaseValueObject


@attr.s(auto_attribs=True, frozen=True)
class PlatformInformation(BaseValueObject):
    name: str
    url: str
