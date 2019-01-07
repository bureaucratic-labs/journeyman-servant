"""Module where views are defined."""

from aiohttp import web
from aiohttp_apispec import docs, use_kwargs, marshal_with

from servant.schema import RequestSchema, ResponseSchema


@docs(tags=['Sentence classification'], description='Endpoint, that does sentence classification')
@use_kwargs(RequestSchema(strict=True))
@marshal_with(ResponseSchema(), 200)
async def index(request):
    """Endpoint, that does sentence classification."""
    items = request['data']['items']
    model = request.app['model']
    result = model.predict(items)
    return web.json_response({
        'result': list(result)
    })
