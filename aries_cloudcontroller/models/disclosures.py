# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Disclosures(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Disclosures - a model defined in OpenAPI

        id: The id of this Disclosures [Optional].
        type: The type of this Disclosures [Optional].
        disclosures: The disclosures of this Disclosures.
    """

    id: Optional[str] = Field(alias="@id", default=None)
    type: Optional[str] = Field(alias="@type", default=None)
    disclosures: List[object] = Field(alias="disclosures")

Disclosures.update_forward_refs()
