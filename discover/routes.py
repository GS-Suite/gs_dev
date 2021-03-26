from responses.invalid_token_response_body import InvalidTokenResponseBody
from responses.standard_response_body import StandardResponseBody
from discover import controllers as discover_controllers
from tokens import controllers as token_controllers


async def search(token, query, filter):
    tkn = await token_controllers.validate_token(token)
    if tkn:
        resp = await discover_controllers.search(query, filter)
        if resp:
            return StandardResponseBody(
                True, "Search results", tkn.token_value, {"results": resp}
            )
        return StandardResponseBody(False, "No search results available", tkn.token_value)
    return InvalidTokenResponseBody()

