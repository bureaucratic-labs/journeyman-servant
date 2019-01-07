"""HTTP API for Journeyman models."""
from journeyman import load_model

from aiohttp import web
from aiohttp_swagger import setup_swagger
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware

from servant import settings
from servant.routes import index


async def swagger(app):
    """Setups online documentation for API."""
    setup_swagger(
        app=app, swagger_url='/api/docs', swagger_info=app['swagger_dict']
    )


async def setup_api_schema(app):
    """Setups API schema."""
    setup_aiohttp_apispec(
        app=app, title='Servant Documentation', version='v1', url='/api/schema'
    )


async def create_app():
    """Create aiohttp application for whole project."""
    app = web.Application()
    app['model'] = load_model(
        model_path=settings.MODEL_PATH,
        preprocessor_path=settings.MODEL_PREPROCESSOR_PATH,
        params_path=settings.MODEL_PARAMS_PATH,
    )
    app.router.add_post('/api/v1/classify', index)
    app.middlewares.append(validation_middleware)
    await setup_api_schema(app)
    app.on_startup.append(swagger)
    return app
