from datetime import datetime, timedelta
from typing import Annotated, Optional
from fastapi import Header
from odmantic import ObjectId
from pydantic import BaseModel, ValidationError
from jose import jwt, JWTError
from core.exceptions import CredentialsException, NotAuthenticatedException

from schemas.visitor import Visitor
from services.visitor import fetch_visitor_by_id
from settings import SETTINGS, Engine


class TokenContent(BaseModel):
    user_id: str


def create_access_token(user: Visitor) -> str:
    token_content = TokenContent(user_id=str(object=user.id))
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode = {"exp": expire, "sub": token_content.model_dump_json()}
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=SETTINGS.SECRET_KEY.get_secret_value(),
        algorithm=SETTINGS.ALGORITHM,
    )
    return str(object=encoded_jwt)


def is_valid_token(token: Annotated[str | None, Header(alias="x-auth-token")] = None) -> bool:
    if token is None:
        raise NotAuthenticatedException()
    try:
        payload = jwt.decode(
            token=token,
            key=SETTINGS.SECRET_KEY.get_secret_value(),
            algorithms=[SETTINGS.ALGORITHM],
        )
    except JWTError:
        raise CredentialsException()

    sub = payload.get("sub")
    if not sub:
        raise CredentialsException()

    # Ensure 'sub' is a string before passing it to model_validate_json
    if not isinstance(sub, str):
        raise CredentialsException()

    try:
        token_content = TokenContent.model_validate_json(sub)
    except ValidationError:
        raise CredentialsException()

    user = fetch_visitor_by_id(Engine, visitor_id=ObjectId(token_content.user_id))

    if user is None:
        raise CredentialsException()

    return True
