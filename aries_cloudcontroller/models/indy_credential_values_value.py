# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IndyCredentialValuesValue(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyCredentialValuesValue - a model defined in OpenAPI

        encoded: The encoded of this IndyCredentialValuesValue.
        raw: The raw of this IndyCredentialValuesValue.
    """

    encoded: str = Field(alias="encoded")
    raw: str = Field(alias="raw")

    @validator("encoded")
    def encoded_pattern(cls, value):
        assert value is not None and re.match(r"^-?[0-9]*$", value)
        return value

IndyCredentialValuesValue.update_forward_refs()
