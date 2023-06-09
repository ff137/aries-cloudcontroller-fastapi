# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.did_create_options import DIDCreateOptions


class DIDCreate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DIDCreate - a model defined in OpenAPI

        method: The method of this DIDCreate [Optional].
        options: The options of this DIDCreate [Optional].
        seed: The seed of this DIDCreate [Optional].
    """

    method: Optional[str] = Field(alias="method", default=None)
    options: Optional[DIDCreateOptions] = Field(alias="options", default=None)
    seed: Optional[str] = Field(alias="seed", default=None)

DIDCreate.update_forward_refs()
