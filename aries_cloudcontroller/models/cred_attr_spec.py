# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CredAttrSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredAttrSpec - a model defined in OpenAPI

        mime_type: The mime_type of this CredAttrSpec [Optional].
        name: The name of this CredAttrSpec.
        value: The value of this CredAttrSpec.
    """

    mime_type: Optional[str] = Field(alias="mime-type", default=None)
    name: str = Field(alias="name")
    value: str = Field(alias="value")

CredAttrSpec.update_forward_refs()
