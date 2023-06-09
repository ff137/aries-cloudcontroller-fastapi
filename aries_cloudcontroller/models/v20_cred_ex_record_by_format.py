# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class V20CredExRecordByFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExRecordByFormat - a model defined in OpenAPI

        cred_issue: The cred_issue of this V20CredExRecordByFormat [Optional].
        cred_offer: The cred_offer of this V20CredExRecordByFormat [Optional].
        cred_proposal: The cred_proposal of this V20CredExRecordByFormat [Optional].
        cred_request: The cred_request of this V20CredExRecordByFormat [Optional].
    """

    cred_issue: Optional[Dict[str, Any]] = Field(alias="cred_issue", default=None)
    cred_offer: Optional[Dict[str, Any]] = Field(alias="cred_offer", default=None)
    cred_proposal: Optional[Dict[str, Any]] = Field(alias="cred_proposal", default=None)
    cred_request: Optional[Dict[str, Any]] = Field(alias="cred_request", default=None)

V20CredExRecordByFormat.update_forward_refs()
