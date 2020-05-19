from __future__ import annotations

import pydantic
import datetime
import asyncio
import typing

from pydantic import BaseModel

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


def make_request(self, petid: int,) -> Pet:
    """Find pet by ID"""
    m = ApiRequest(
        method="GET",
        path="/api/v3/pet/{petId}".format(petId=petid,),
        content_type=None,
        body=None,
        headers=self._only_provided({}, exclude_none=True),
        query_params=self._only_provided({}, exclude_none=True),
        cookies=self._only_provided({}, exclude_none=True),
    )
    return self.make_request(
        {"200": {"application/json": Pet, "application/xml": Pet,},}, m
    )
