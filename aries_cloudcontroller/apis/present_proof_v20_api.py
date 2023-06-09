# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from aries_cloudcontroller.apis.present_proof_v20_api_base import BasePresentProofV20Api
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from aries_cloudcontroller.models.extra_models import TokenModel  # noqa: F401
from aries_cloudcontroller.models.indy_cred_precis import IndyCredPrecis
from aries_cloudcontroller.models.v20_pres_create_request_request import V20PresCreateRequestRequest
from aries_cloudcontroller.models.v20_pres_ex_record import V20PresExRecord
from aries_cloudcontroller.models.v20_pres_ex_record_list import V20PresExRecordList
from aries_cloudcontroller.models.v20_pres_problem_report_request import V20PresProblemReportRequest
from aries_cloudcontroller.models.v20_pres_proposal_request import V20PresProposalRequest
from aries_cloudcontroller.models.v20_pres_send_request_request import V20PresSendRequestRequest
from aries_cloudcontroller.models.v20_pres_spec_by_format_request import V20PresSpecByFormatRequest
from aries_cloudcontroller.models.v20_presentation_send_request_to_proposal import V20PresentationSendRequestToProposal
from aries_cloudcontroller.security_api import get_token_AuthorizationHeader

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/present-proof-2.0/create-request",
    responses={
        200: {"model": V20PresExRecord, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Creates a presentation request not bound to any proposal or connection",
    response_model_by_alias=True,
)
async def create_proof_request(
    body: V20PresCreateRequestRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20PresExRecord:
    ...


@router.delete(
    "/present-proof-2.0/records/{pres_ex_id}",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Remove an existing presentation exchange record",
    response_model_by_alias=True,
)
async def delete_pres_ex_record(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.get(
    "/present-proof-2.0/records",
    responses={
        200: {"model": V20PresExRecordList, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Fetch all present-proof exchange records",
    response_model_by_alias=True,
)
async def get_matching_pres_ex_records(
    connection_id: str = Query(None, description="Connection identifier"),
    role: str = Query(None, description="Role assigned in presentation exchange"),
    state: str = Query(None, description="Presentation exchange state"),
    thread_id: str = Query(None, description="Thread identifier"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20PresExRecordList:
    ...


@router.get(
    "/present-proof-2.0/records/{pres_ex_id}/credentials",
    responses={
        200: {"model": List[IndyCredPrecis], "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Fetch credentials from wallet for presentation request",
    response_model_by_alias=True,
)
async def get_pres_ex_credentials(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    count: str = Query(None, description="Maximum number to retrieve", regex=r"^[1-9][0-9]*$"),
    extra_query: str = Query(None, description="(JSON) object mapping referents to extra WQL queries", regex=r"^{\s*&quot;.*?&quot;\s*:\s*{.*?}\s*(,\s*&quot;.*?&quot;\s*:\s*{.*?}\s*)*\s*}$"),
    referent: str = Query(None, description="Proof request referents of interest, comma-separated"),
    start: str = Query(None, description="Start index", regex=r"^[0-9]*$"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> List[IndyCredPrecis]:
    ...


@router.get(
    "/present-proof-2.0/records/{pres_ex_id}",
    responses={
        200: {"model": V20PresExRecord, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Fetch a single presentation exchange record",
    response_model_by_alias=True,
)
async def get_pres_ex_record(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20PresExRecord:
    ...


@router.post(
    "/present-proof-2.0/records/{pres_ex_id}/problem-report",
    responses={
        200: {"model": object, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Send a problem report for presentation exchange",
    response_model_by_alias=True,
)
async def report_pres_ex_problem(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V20PresProblemReportRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> object:
    ...


@router.post(
    "/present-proof-2.0/send-request",
    responses={
        200: {"model": V20PresExRecord, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Sends a free presentation request not bound to any proposal",
    response_model_by_alias=True,
)
async def send_free_presentation_request(
    body: V20PresSendRequestRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20PresExRecord:
    ...


@router.post(
    "/present-proof-2.0/send-proposal",
    responses={
        200: {"model": V20PresExRecord, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Sends a presentation proposal",
    response_model_by_alias=True,
)
async def send_presentation_proposal(
    body: V20PresProposalRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20PresExRecord:
    ...


@router.post(
    "/present-proof-2.0/records/{pres_ex_id}/send-presentation",
    responses={
        200: {"model": V20PresExRecord, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Sends a proof presentation",
    response_model_by_alias=True,
)
async def send_proof_presentation(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V20PresSpecByFormatRequest = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20PresExRecord:
    ...


@router.post(
    "/present-proof-2.0/records/{pres_ex_id}/send-request",
    responses={
        200: {"model": V20PresExRecord, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Sends a presentation request in reference to a proposal",
    response_model_by_alias=True,
)
async def send_proof_presentation_request(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    body: V20PresentationSendRequestToProposal = Body(None, description=""),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20PresExRecord:
    ...


@router.post(
    "/present-proof-2.0/records/{pres_ex_id}/verify-presentation",
    responses={
        200: {"model": V20PresExRecord, "description": ""},
    },
    tags=["present-proof v2.0"],
    summary="Verify a received presentation",
    response_model_by_alias=True,
)
async def verify_received_presentation(
    pres_ex_id: str = Path(None, description="Presentation exchange identifier", regex=r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"),
    token_AuthorizationHeader: TokenModel = Security(
        get_token_AuthorizationHeader
    ),
) -> V20PresExRecord:
    ...
