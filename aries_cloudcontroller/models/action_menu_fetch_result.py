# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.action_menu_fetch_result_result import ActionMenuFetchResultResult


class ActionMenuFetchResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ActionMenuFetchResult - a model defined in OpenAPI

        result: The result of this ActionMenuFetchResult [Optional].
    """

    result: Optional[ActionMenuFetchResultResult] = Field(alias="result", default=None)

ActionMenuFetchResult.update_forward_refs()
