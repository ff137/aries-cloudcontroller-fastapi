# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class KeylistQueryFilterRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    KeylistQueryFilterRequest - a model defined in OpenAPI

        filter: The filter of this KeylistQueryFilterRequest [Optional].
    """

    filter: Optional[Dict[str, Any]] = Field(alias="filter", default=None)

KeylistQueryFilterRequest.update_forward_refs()
