# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.models.v20_cred_format import V20CredFormat
from aries_cloudcontroller.models.v20_cred_proposal_credential_preview import V20CredProposalCredentialPreview


class V20CredExRecordCredProposal(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExRecordCredProposal - a model defined in OpenAPI

        id: The id of this V20CredExRecordCredProposal [Optional].
        type: The type of this V20CredExRecordCredProposal [Optional].
        comment: The comment of this V20CredExRecordCredProposal [Optional].
        credential_preview: The credential_preview of this V20CredExRecordCredProposal [Optional].
        filtersattach: The filtersattach of this V20CredExRecordCredProposal.
        formats: The formats of this V20CredExRecordCredProposal.
    """

    id: Optional[str] = Field(alias="@id", default=None)
    type: Optional[str] = Field(alias="@type", default=None)
    comment: Optional[str] = Field(alias="comment", default=None)
    credential_preview: Optional[V20CredProposalCredentialPreview] = Field(alias="credential_preview", default=None)
    filtersattach: List[AttachDecorator] = Field(alias="filters~attach")
    formats: List[V20CredFormat] = Field(alias="formats")

V20CredExRecordCredProposal.update_forward_refs()
