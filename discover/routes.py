from responses.invalid_token_response_body import InvalidTokenResponseBody
from responses.standard_response_body import StandardResponseBody
from discover import controllers as discover_controllers
from tokens import controllers as token_controllers


async def search(token, query, filter):
    resp = await discover_controllers.search(query, filter)
    if resp:
        return StandardResponseBody(
            True, "Search results", token.token_value, {"results": resp}
        )
    return StandardResponseBody(False, "No search results available", token.token_value)

