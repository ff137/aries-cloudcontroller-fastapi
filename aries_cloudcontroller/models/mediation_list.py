# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.mediation_record import MediationRecord


class MediationList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MediationList - a model defined in OpenAPI

        results: The results of this MediationList [Optional].
    """

    results: Optional[List[MediationRecord]] = Field(alias="results", default=None)

MediationList.update_forward_refs()