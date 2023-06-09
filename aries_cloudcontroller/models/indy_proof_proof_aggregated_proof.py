# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IndyProofProofAggregatedProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofProofAggregatedProof - a model defined in OpenAPI

        c_hash: The c_hash of this IndyProofProofAggregatedProof [Optional].
        c_list: The c_list of this IndyProofProofAggregatedProof [Optional].
    """

    c_hash: Optional[str] = Field(alias="c_hash", default=None)
    c_list: Optional[List[List[int]]] = Field(alias="c_list", default=None)

IndyProofProofAggregatedProof.update_forward_refs()
