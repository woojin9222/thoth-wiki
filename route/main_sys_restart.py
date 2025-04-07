from .tool.func import *

async def main_sys_restart_do():
    print('Restart')

    python_ver = ''
    python_ver = str(sys.version_info.major) + '.' + str(sys.version_info.minor)

    run_list = [sys.executable, 'python' + python_ver, 'python3', 'python', 'py -' + python_ver]
    for exe_name in run_list:
        try:
            os.execl(exe_name, sys.executable, *sys.argv)
        except:
            pass

        try:
            os.execl(exe_name, '"' + sys.executable + '"', *sys.argv)
        except:
            pass

        try:
            os.execl(exe_name, os.path.abspath(__file__), *sys.argv)
        except:
            pass
    else:
        return 0

async def main_sys_restart(golang_process):
    with get_db_connect() as conn:
        if await acl_check('', 'owner_auth', '', '') == 1:
            return await re_error(conn, 3)

        if flask.request.method == 'POST':
            await acl_check(tool = 'owner_auth', memo = 'restart')

            if golang_process.poll() is None:
                golang_process.terminate()
                try:
                    golang_process.wait(timeout = 5)
                except subprocess.TimeoutExpired:
                    golang_process.kill()

            if await main_sys_restart_do() == 0:
                return await re_error(conn, 33)
        else:
            return easy_minify(conn, flask.render_template(skin_check(conn),
                imp = [get_lang(conn, 'wiki_restart'), wiki_set(conn), await wiki_custom(conn), wiki_css([0, 0])],
                data = '<button type="submit">' + get_lang(conn, 'restart') + '</button>',
                menu = [['manager', get_lang(conn, 'return')]]
            ))