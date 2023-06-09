# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IndyKeyCorrectnessProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyKeyCorrectnessProof - a model defined in OpenAPI

        c: The c of this IndyKeyCorrectnessProof.
        xr_cap: The xr_cap of this IndyKeyCorrectnessProof.
        xz_cap: The xz_cap of this IndyKeyCorrectnessProof.
    """

    c: str = Field(alias="c")
    xr_cap: List[List[str]] = Field(alias="xr_cap")
    xz_cap: str = Field(alias="xz_cap")

    @validator("c")
    def c_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9]*$", value)
        return value

    @validator("xz_cap")
    def xz_cap_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9]*$", value)
        return value

IndyKeyCorrectnessProof.update_forward_refs()
