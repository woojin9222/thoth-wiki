from .tool.func import *

async def api_func_email():
    if flask.request.method == 'POST':
        func_name = sys._getframe().f_code.co_name
        func_name += '_post'

        other_set = {}
        other_set["ip"] = ip_check()
        other_set["who"] = flask.request.form.get('email', '')
        other_set["title"] = flask.request.form.get('title', '')
        other_set["data"] = flask.request.form.get('data', '')

        return flask.Response(response = (await python_to_golang(func_name, other_set)), status = 200, mimetype = 'application/json')
    else:
        return flask.jsonify({}) 