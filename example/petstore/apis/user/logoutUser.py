from __future__ import annotations

import pydantic
import datetime
import asyncio
import typing

from pydantic import BaseModel

from swagger_codegen.api.request import ApiRequest


def make_request(self,) -> None:
    """Logs out current logged in user session"""
    m = ApiRequest(
        method="GET",
        path="/api/v3/user/logout".format(),
        content_type=None,
        body=None,
        headers=self._only_provided({}),
        query_params=self._only_provided({}),
        cookies=self._only_provided({}),
    )
    return self.make_request({}, m)
