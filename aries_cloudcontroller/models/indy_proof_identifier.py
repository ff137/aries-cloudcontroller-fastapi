# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IndyProofIdentifier(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofIdentifier - a model defined in OpenAPI

        cred_def_id: The cred_def_id of this IndyProofIdentifier [Optional].
        rev_reg_id: The rev_reg_id of this IndyProofIdentifier [Optional].
        schema_id: The schema_id of this IndyProofIdentifier [Optional].
        timestamp: The timestamp of this IndyProofIdentifier [Optional].
    """

    cred_def_id: Optional[str] = Field(alias="cred_def_id", default=None)
    rev_reg_id: Optional[str] = Field(alias="rev_reg_id", default=None)
    schema_id: Optional[str] = Field(alias="schema_id", default=None)
    timestamp: Optional[int] = Field(alias="timestamp", default=None)

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        assert value is not None and re.match(r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$", value)
        return value

    @validator("rev_reg_id")
    def rev_reg_id_pattern(cls, value):
        assert value is not None and re.match(r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)", value)
        return value

    @validator("schema_id")
    def schema_id_pattern(cls, value):
        assert value is not None and re.match(r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$", value)
        return value

    @validator("timestamp")
    def timestamp_max(cls, value):
        assert value <= -1
        return value

    @validator("timestamp")
    def timestamp_min(cls, value):
        assert value >= 0
        return value

IndyProofIdentifier.update_forward_refs()
