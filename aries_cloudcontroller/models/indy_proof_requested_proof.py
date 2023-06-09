# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.indy_proof_requested_proof_predicate import IndyProofRequestedProofPredicate
from aries_cloudcontroller.models.indy_proof_requested_proof_revealed_attr import IndyProofRequestedProofRevealedAttr
from aries_cloudcontroller.models.indy_proof_requested_proof_revealed_attr_group import IndyProofRequestedProofRevealedAttrGroup


class IndyProofRequestedProof(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofRequestedProof - a model defined in OpenAPI

        predicates: The predicates of this IndyProofRequestedProof [Optional].
        revealed_attr_groups: The revealed_attr_groups of this IndyProofRequestedProof [Optional].
        revealed_attrs: The revealed_attrs of this IndyProofRequestedProof [Optional].
        self_attested_attrs: The self_attested_attrs of this IndyProofRequestedProof [Optional].
        unrevealed_attrs: The unrevealed_attrs of this IndyProofRequestedProof [Optional].
    """

    predicates: Optional[Dict[str, IndyProofRequestedProofPredicate]] = Field(alias="predicates", default=None)
    revealed_attr_groups: Optional[Dict[str, IndyProofRequestedProofRevealedAttrGroup]] = Field(alias="revealed_attr_groups", default=None)
    revealed_attrs: Optional[Dict[str, IndyProofRequestedProofRevealedAttr]] = Field(alias="revealed_attrs", default=None)
    self_attested_attrs: Optional[Dict[str, Any]] = Field(alias="self_attested_attrs", default=None)
    unrevealed_attrs: Optional[Dict[str, Any]] = Field(alias="unrevealed_attrs", default=None)

IndyProofRequestedProof.update_forward_refs()
