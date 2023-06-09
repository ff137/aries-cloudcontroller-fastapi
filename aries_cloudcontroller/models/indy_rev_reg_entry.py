# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.indy_rev_reg_entry_value import IndyRevRegEntryValue


class IndyRevRegEntry(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyRevRegEntry - a model defined in OpenAPI

        value: The value of this IndyRevRegEntry [Optional].
        ver: The ver of this IndyRevRegEntry [Optional].
    """

    value: Optional[IndyRevRegEntryValue] = Field(alias="value", default=None)
    ver: Optional[str] = Field(alias="ver", default=None)

    @validator("ver")
    def ver_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9.]+$", value)
        return value

IndyRevRegEntry.update_forward_refs()
