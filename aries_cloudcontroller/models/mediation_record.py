# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class MediationRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MediationRecord - a model defined in OpenAPI

        connection_id: The connection_id of this MediationRecord.
        created_at: The created_at of this MediationRecord [Optional].
        endpoint: The endpoint of this MediationRecord [Optional].
        mediation_id: The mediation_id of this MediationRecord [Optional].
        mediator_terms: The mediator_terms of this MediationRecord [Optional].
        recipient_terms: The recipient_terms of this MediationRecord [Optional].
        role: The role of this MediationRecord.
        routing_keys: The routing_keys of this MediationRecord [Optional].
        state: The state of this MediationRecord [Optional].
        updated_at: The updated_at of this MediationRecord [Optional].
    """

    connection_id: str = Field(alias="connection_id")
    created_at: Optional[str] = Field(alias="created_at", default=None)
    endpoint: Optional[str] = Field(alias="endpoint", default=None)
    mediation_id: Optional[str] = Field(alias="mediation_id", default=None)
    mediator_terms: Optional[List[str]] = Field(alias="mediator_terms", default=None)
    recipient_terms: Optional[List[str]] = Field(alias="recipient_terms", default=None)
    role: str = Field(alias="role")
    routing_keys: Optional[List[str]] = Field(alias="routing_keys", default=None)
    state: Optional[str] = Field(alias="state", default=None)
    updated_at: Optional[str] = Field(alias="updated_at", default=None)

    @validator("created_at")
    def created_at_pattern(cls, value):
        assert value is not None and re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value)
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        assert value is not None and re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value)
        return value

MediationRecord.update_forward_refs()
