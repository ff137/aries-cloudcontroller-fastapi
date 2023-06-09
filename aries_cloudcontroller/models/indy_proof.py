# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.indy_proof_identifier import IndyProofIdentifier
from aries_cloudcontroller.models.indy_proof_proof import IndyProofProof
from aries_cloudcontroller.models.indy_proof_requested_proof import IndyProofRequestedProof


class IndyProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProof - a model defined in OpenAPI

        identifiers: The identifiers of this IndyProof [Optional].
        proof: The proof of this IndyProof [Optional].
        requested_proof: The requested_proof of this IndyProof [Optional].
    """

    identifiers: Optional[List[IndyProofIdentifier]] = Field(alias="identifiers", default=None)
    proof: Optional[IndyProofProof] = Field(alias="proof", default=None)
    requested_proof: Optional[IndyProofRequestedProof] = Field(alias="requested_proof", default=None)

IndyProof.update_forward_refs()
