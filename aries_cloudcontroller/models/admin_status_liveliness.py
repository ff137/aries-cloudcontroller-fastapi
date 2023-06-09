# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class AdminStatusLiveliness(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AdminStatusLiveliness - a model defined in OpenAPI

        alive: The alive of this AdminStatusLiveliness [Optional].
    """

    alive: Optional[bool] = Field(alias="alive", default=None)

AdminStatusLiveliness.update_forward_refs()
