# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from aries_cloudcontroller.models.publish_revocations import PublishRevocations
from aries_cloudcontroller.models.txn_or_publish_revocations_result_txn import TxnOrPublishRevocationsResultTxn


class TxnOrPublishRevocationsResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TxnOrPublishRevocationsResult - a model defined in OpenAPI

        sent: The sent of this TxnOrPublishRevocationsResult [Optional].
        txn: The txn of this TxnOrPublishRevocationsResult [Optional].
    """

    sent: Optional[PublishRevocations] = Field(alias="sent", default=None)
    txn: Optional[TxnOrPublishRevocationsResultTxn] = Field(alias="txn", default=None)

TxnOrPublishRevocationsResult.update_forward_refs()
