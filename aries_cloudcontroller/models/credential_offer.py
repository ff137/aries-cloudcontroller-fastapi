# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.models.credential_preview import CredentialPreview


class CredentialOffer(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredentialOffer - a model defined in OpenAPI

        id: The id of this CredentialOffer [Optional].
        type: The type of this CredentialOffer [Optional].
        comment: The comment of this CredentialOffer [Optional].
        credential_preview: The credential_preview of this CredentialOffer [Optional].
        offersattach: The offersattach of this CredentialOffer.
    """

    id: Optional[str] = Field(alias="@id", default=None)
    type: Optional[str] = Field(alias="@type", default=None)
    comment: Optional[str] = Field(alias="comment", default=None)
    credential_preview: Optional[CredentialPreview] = Field(alias="credential_preview", default=None)
    offersattach: List[AttachDecorator] = Field(alias="offers~attach")

CredentialOffer.update_forward_refs()
