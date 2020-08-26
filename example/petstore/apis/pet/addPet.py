from __future__ import annotations

import pydantic
import datetime
import asyncio
import typing

from pydantic import BaseModel

from swagger_codegen.api.base import BaseApi
from swagger_codegen.api.request import ApiRequest


class Tag(BaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None


class Category(BaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None


class Pet(BaseModel):
    category: typing.Optional[Category] = None
    id: typing.Optional[int] = None
    name: str
    photoUrls: typing.List[str]
    status: typing.Optional[str] = None
    tags: typing.Optional[typing.List[Tag]] = None


def make_request(self: BaseApi, __request__: Pet,) -> Pet:
    """Add a new pet to the store"""

    def serialize_item(item):
        if isinstance(item, pydantic.BaseModel):
            return item.dict()
        return item

    if isinstance(__request__, (list, tuple, set)):
        body = [serialize_item(item) for item in __request__]
    else:
        body = __request__.dict()

    m = ApiRequest(
        method="POST",
        path="/api/v3/pet".format(),
        content_type="application/json",
        body=body,
        headers=self._only_provided({}),
        query_params=self._only_provided({}),
        cookies=self._only_provided({}),
    )
    return self.make_request(
        {
            "200": {"application/json": Pet, "application/xml": Pet,},
            "405": {"default": None,},
        },
        m,
    )
