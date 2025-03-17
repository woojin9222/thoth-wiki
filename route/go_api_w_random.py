from .tool.func import *

async def api_w_random():
    return await python_to_golang(sys._getframe().f_code.co_name)

async def api_w_random_exter():
    return flask.Response(response = await api_w_random(), status = 200, mimetype = 'application/json')