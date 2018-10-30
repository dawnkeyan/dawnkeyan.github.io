# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1540884782.2380002
_enable_loop = True
_template_filename = 'd:/workspace/python/nikola/nikola/data/themes/base/templates/comments_helper_commento.tmpl'
_template_uri = 'comments_helper_commento.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\r\n    <div id="commento"></div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<script src="')
        __M_writer(str(comment_system_id))
        __M_writer('/assets/js/commento.min.js"></script>\r\n<script>\r\nwindow.onload = function() {\r\n    Commento.init({\r\n        serverUrl: "')
        __M_writer(str(comment_system_id))
        __M_writer('",\r\n    });\r\n}\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "d:/workspace/python/nikola/nikola/data/themes/base/templates/comments_helper_commento.tmpl", "uri": "comments_helper_commento.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 4, "22": 7, "23": 19, "29": 2, "33": 2, "39": 6, "43": 6, "49": 10, "54": 10, "55": 11, "56": 11, "57": 15, "58": 15, "64": 58}}
__M_END_METADATA
"""