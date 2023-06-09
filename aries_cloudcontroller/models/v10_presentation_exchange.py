# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.v10_presentation_exchange_presentation import V10PresentationExchangePresentation
from aries_cloudcontroller.models.v10_presentation_exchange_presentation_proposal_dict import V10PresentationExchangePresentationProposalDict
from aries_cloudcontroller.models.v10_presentation_exchange_presentation_request import V10PresentationExchangePresentationRequest
from aries_cloudcontroller.models.v10_presentation_exchange_presentation_request_dict import V10PresentationExchangePresentationRequestDict


class V10PresentationExchange(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10PresentationExchange - a model defined in OpenAPI

        auto_present: The auto_present of this V10PresentationExchange [Optional].
        auto_verify: The auto_verify of this V10PresentationExchange [Optional].
        connection_id: The connection_id of this V10PresentationExchange [Optional].
        created_at: The created_at of this V10PresentationExchange [Optional].
        error_msg: The error_msg of this V10PresentationExchange [Optional].
        initiator: The initiator of this V10PresentationExchange [Optional].
        presentation: The presentation of this V10PresentationExchange [Optional].
        presentation_exchange_id: The presentation_exchange_id of this V10PresentationExchange [Optional].
        presentation_proposal_dict: The presentation_proposal_dict of this V10PresentationExchange [Optional].
        presentation_request: The presentation_request of this V10PresentationExchange [Optional].
        presentation_request_dict: The presentation_request_dict of this V10PresentationExchange [Optional].
        role: The role of this V10PresentationExchange [Optional].
        state: The state of this V10PresentationExchange [Optional].
        thread_id: The thread_id of this V10PresentationExchange [Optional].
        trace: The trace of this V10PresentationExchange [Optional].
        updated_at: The updated_at of this V10PresentationExchange [Optional].
        verified: The verified of this V10PresentationExchange [Optional].
        verified_msgs: The verified_msgs of this V10PresentationExchange [Optional].
    """

    auto_present: Optional[bool] = Field(alias="auto_present", default=None)
    auto_verify: Optional[bool] = Field(alias="auto_verify", default=None)
    connection_id: Optional[str] = Field(alias="connection_id", default=None)
    created_at: Optional[str] = Field(alias="created_at", default=None)
    error_msg: Optional[str] = Field(alias="error_msg", default=None)
    initiator: Optional[str] = Field(alias="initiator", default=None)
    presentation: Optional[V10PresentationExchangePresentation] = Field(alias="presentation", default=None)
    presentation_exchange_id: Optional[str] = Field(alias="presentation_exchange_id", default=None)
    presentation_proposal_dict: Optional[V10PresentationExchangePresentationProposalDict] = Field(alias="presentation_proposal_dict", default=None)
    presentation_request: Optional[V10PresentationExchangePresentationRequest] = Field(alias="presentation_request", default=None)
    presentation_request_dict: Optional[V10PresentationExchangePresentationRequestDict] = Field(alias="presentation_request_dict", default=None)
    role: Optional[str] = Field(alias="role", default=None)
    state: Optional[str] = Field(alias="state", default=None)
    thread_id: Optional[str] = Field(alias="thread_id", default=None)
    trace: Optional[bool] = Field(alias="trace", default=None)
    updated_at: Optional[str] = Field(alias="updated_at", default=None)
    verified: Optional[str] = Field(alias="verified", default=None)
    verified_msgs: Optional[List[str]] = Field(alias="verified_msgs", default=None)

    @validator("created_at")
    def created_at_pattern(cls, value):
        assert value is not None and re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value)
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        assert value is not None and re.match(r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$", value)
        return value

V10PresentationExchange.update_forward_refs()
