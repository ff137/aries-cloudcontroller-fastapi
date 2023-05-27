# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.issuer_cred_rev_record import IssuerCredRevRecord


class CredRevRecordResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredRevRecordResult - a model defined in OpenAPI

        result: The result of this CredRevRecordResult [Optional].
    """

    result: Optional[IssuerCredRevRecord] = Field(alias="result", default=None)

CredRevRecordResult.update_forward_refs()