# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class DIDCreateOptions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DIDCreateOptions - a model defined in OpenAPI

        did: The did of this DIDCreateOptions [Optional].
        key_type: The key_type of this DIDCreateOptions.
    """

    did: Optional[str] = Field(alias="did", default=None)
    key_type: str = Field(alias="key_type")

    @validator("did")
    def did_pattern(cls, value):
        assert value is not None and re.match(r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$|^did:([a-zA-Z0-9_]+):([a-zA-Z0-9_.%-]+(:[a-zA-Z0-9_.%-]+)*)((;[a-zA-Z0-9_.:%-]+&#x3D;[a-zA-Z0-9_.:%-]*)*)(\\/[^#?]*)?([?][^#]*)?(\#.*)?$$", value)
        return value

DIDCreateOptions.update_forward_refs()
