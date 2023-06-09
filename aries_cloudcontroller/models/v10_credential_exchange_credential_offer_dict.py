# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.models.credential_preview import CredentialPreview


class V10CredentialExchangeCredentialOfferDict(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10CredentialExchangeCredentialOfferDict - a model defined in OpenAPI

        id: The id of this V10CredentialExchangeCredentialOfferDict [Optional].
        type: The type of this V10CredentialExchangeCredentialOfferDict [Optional].
        comment: The comment of this V10CredentialExchangeCredentialOfferDict [Optional].
        credential_preview: The credential_preview of this V10CredentialExchangeCredentialOfferDict [Optional].
        offersattach: The offersattach of this V10CredentialExchangeCredentialOfferDict.
    """

    id: Optional[str] = Field(alias="@id", default=None)
    type: Optional[str] = Field(alias="@type", default=None)
    comment: Optional[str] = Field(alias="comment", default=None)
    credential_preview: Optional[CredentialPreview] = Field(alias="credential_preview", default=None)
    offersattach: List[AttachDecorator] = Field(alias="offers~attach")

V10CredentialExchangeCredentialOfferDict.update_forward_refs()
