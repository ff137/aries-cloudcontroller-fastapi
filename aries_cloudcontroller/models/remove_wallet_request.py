# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class RemoveWalletRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RemoveWalletRequest - a model defined in OpenAPI

        wallet_key: The wallet_key of this RemoveWalletRequest [Optional].
    """

    wallet_key: Optional[str] = Field(alias="wallet_key", default=None)

RemoveWalletRequest.update_forward_refs()