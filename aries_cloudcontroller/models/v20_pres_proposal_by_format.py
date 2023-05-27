# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.v20_pres_proposal_by_format_dif import V20PresProposalByFormatDif
from aries_cloudcontroller.models.v20_pres_proposal_by_format_indy import V20PresProposalByFormatIndy


class V20PresProposalByFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresProposalByFormat - a model defined in OpenAPI

        dif: The dif of this V20PresProposalByFormat [Optional].
        indy: The indy of this V20PresProposalByFormat [Optional].
    """

    dif: Optional[V20PresProposalByFormatDif] = Field(alias="dif", default=None)
    indy: Optional[V20PresProposalByFormatIndy] = Field(alias="indy", default=None)

V20PresProposalByFormat.update_forward_refs()