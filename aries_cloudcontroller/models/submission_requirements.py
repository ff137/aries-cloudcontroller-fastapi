# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SubmissionRequirements(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SubmissionRequirements - a model defined in OpenAPI

        count: The count of this SubmissionRequirements [Optional].
        _from: The _from of this SubmissionRequirements [Optional].
        from_nested: The from_nested of this SubmissionRequirements [Optional].
        max: The max of this SubmissionRequirements [Optional].
        min: The min of this SubmissionRequirements [Optional].
        name: The name of this SubmissionRequirements [Optional].
        purpose: The purpose of this SubmissionRequirements [Optional].
        rule: The rule of this SubmissionRequirements [Optional].
    """

    count: Optional[int] = Field(alias="count", default=None)
    _from: Optional[str] = Field(alias="from", default=None)
    from_nested: Optional[List[SubmissionRequirements]] = Field(alias="from_nested", default=None)
    max: Optional[int] = Field(alias="max", default=None)
    min: Optional[int] = Field(alias="min", default=None)
    name: Optional[str] = Field(alias="name", default=None)
    purpose: Optional[str] = Field(alias="purpose", default=None)
    rule: Optional[str] = Field(alias="rule", default=None)

SubmissionRequirements.update_forward_refs()
