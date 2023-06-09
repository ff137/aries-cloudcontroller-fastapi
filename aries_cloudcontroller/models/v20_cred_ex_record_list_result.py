# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.v20_cred_ex_record_detail import V20CredExRecordDetail


class V20CredExRecordListResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExRecordListResult - a model defined in OpenAPI

        results: The results of this V20CredExRecordListResult [Optional].
    """

    results: Optional[List[V20CredExRecordDetail]] = Field(alias="results", default=None)

V20CredExRecordListResult.update_forward_refs()
