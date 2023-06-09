# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.signed_doc_proof import SignedDocProof


class VerifyRequestDoc(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    VerifyRequestDoc - a model defined in OpenAPI

        proof: The proof of this VerifyRequestDoc.
    """

    proof: SignedDocProof = Field(alias="proof")

VerifyRequestDoc.update_forward_refs()
