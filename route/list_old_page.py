from .tool.func import *

async def list_old_page(num = 1, set_type = 'old'):
    with get_db_connect() as conn:
        title = ''
        if set_type == 'old':
            title = get_lang(conn, 'old_page')
        else:
            title = get_lang(conn, 'new_page')

        return easy_minify(conn, flask.render_template(skin_check(conn),
            imp = [title, wiki_set(conn), await wiki_custom(conn), wiki_css([0, 0])],
            data = '',
            menu = [['other', get_lang(conn, 'return')]]
        ))