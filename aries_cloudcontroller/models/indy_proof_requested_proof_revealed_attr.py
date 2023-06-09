# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IndyProofRequestedProofRevealedAttr(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofRequestedProofRevealedAttr - a model defined in OpenAPI

        encoded: The encoded of this IndyProofRequestedProofRevealedAttr [Optional].
        raw: The raw of this IndyProofRequestedProofRevealedAttr [Optional].
        sub_proof_index: The sub_proof_index of this IndyProofRequestedProofRevealedAttr [Optional].
    """

    encoded: Optional[str] = Field(alias="encoded", default=None)
    raw: Optional[str] = Field(alias="raw", default=None)
    sub_proof_index: Optional[int] = Field(alias="sub_proof_index", default=None)

    @validator("encoded")
    def encoded_pattern(cls, value):
        assert value is not None and re.match(r"^-?[0-9]*$", value)
        return value

IndyProofRequestedProofRevealedAttr.update_forward_refs()
