# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.v20_pres_request_by_format_dif import V20PresRequestByFormatDif
from aries_cloudcontroller.models.v20_pres_request_by_format_indy import V20PresRequestByFormatIndy


class V20PresRequestByFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresRequestByFormat - a model defined in OpenAPI

        dif: The dif of this V20PresRequestByFormat [Optional].
        indy: The indy of this V20PresRequestByFormat [Optional].
    """

    dif: Optional[V20PresRequestByFormatDif] = Field(alias="dif", default=None)
    indy: Optional[V20PresRequestByFormatIndy] = Field(alias="indy", default=None)

V20PresRequestByFormat.update_forward_refs()
