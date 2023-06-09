# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.conn_record import ConnRecord


class ConnectionStaticResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ConnectionStaticResult - a model defined in OpenAPI

        my_did: The my_did of this ConnectionStaticResult.
        my_endpoint: The my_endpoint of this ConnectionStaticResult.
        my_verkey: The my_verkey of this ConnectionStaticResult.
        record: The record of this ConnectionStaticResult.
        their_did: The their_did of this ConnectionStaticResult.
        their_verkey: The their_verkey of this ConnectionStaticResult.
    """

    my_did: str = Field(alias="my_did")
    my_endpoint: str = Field(alias="my_endpoint")
    my_verkey: str = Field(alias="my_verkey")
    record: ConnRecord = Field(alias="record")
    their_did: str = Field(alias="their_did")
    their_verkey: str = Field(alias="their_verkey")

    @validator("my_did")
    def my_did_pattern(cls, value):
        assert value is not None and re.match(r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$", value)
        return value

    @validator("my_endpoint")
    def my_endpoint_pattern(cls, value):
        assert value is not None and re.match(r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&amp;#]+)?$", value)
        return value

    @validator("my_verkey")
    def my_verkey_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$", value)
        return value

    @validator("their_did")
    def their_did_pattern(cls, value):
        assert value is not None and re.match(r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$", value)
        return value

    @validator("their_verkey")
    def their_verkey_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$", value)
        return value

ConnectionStaticResult.update_forward_refs()
