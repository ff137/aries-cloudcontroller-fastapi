# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.credential_preview import CredentialPreview


class V10CredentialConnFreeOfferRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialConnFreeOfferRequest - a model defined in OpenAPI

        auto_issue: The auto_issue of this V10CredentialConnFreeOfferRequest [Optional].
        auto_remove: The auto_remove of this V10CredentialConnFreeOfferRequest [Optional].
        comment: The comment of this V10CredentialConnFreeOfferRequest [Optional].
        cred_def_id: The cred_def_id of this V10CredentialConnFreeOfferRequest.
        credential_preview: The credential_preview of this V10CredentialConnFreeOfferRequest.
        trace: The trace of this V10CredentialConnFreeOfferRequest [Optional].
    """

    auto_issue: Optional[bool] = Field(alias="auto_issue", default=None)
    auto_remove: Optional[bool] = Field(alias="auto_remove", default=None)
    comment: Optional[str] = Field(alias="comment", default=None)
    cred_def_id: str = Field(alias="cred_def_id")
    credential_preview: CredentialPreview = Field(alias="credential_preview")
    trace: Optional[bool] = Field(alias="trace", default=None)

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        assert value is not None and re.match(r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$", value)
        return value

V10CredentialConnFreeOfferRequest.update_forward_refs()
