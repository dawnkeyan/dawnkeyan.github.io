# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1540910613.0769725
_enable_loop = True
_template_filename = 'themes/bootstrap3/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        hidden_tags = _import_ns.get('hidden_tags', context.get('hidden_tags', UNDEFINED))
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        cat_items = _import_ns.get('cat_items', context.get('cat_items', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        cat_hierarchy = _import_ns.get('cat_hierarchy', context.get('cat_hierarchy', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(feeds_translations.head(kind=kind, feeds=False)))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        hidden_tags = _import_ns.get('hidden_tags', context.get('hidden_tags', UNDEFINED))
        items = _import_ns.get('items', context.get('items', UNDEFINED))
        cat_items = _import_ns.get('cat_items', context.get('cat_items', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        def content():
            return render_content(context)
        cat_hierarchy = _import_ns.get('cat_hierarchy', context.get('cat_hierarchy', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n<h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\r\n<div class="metadata">\r\n    ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\r\n</div>\r\n')
        if cat_items:
            if items:
                __M_writer('        <h2>')
                __M_writer(str(messages("Categories")))
                __M_writer('</h2>\r\n')
            for text, full_name, path, link, indent_levels, indent_change_before, indent_change_after in cat_hierarchy:
                for i in range(indent_change_before):
                    __M_writer('            <ul class="list-inline">\r\n')
                __M_writer('        <li><a class="reference badge" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(text)))
                __M_writer('</a>\r\n')
                if indent_change_after <= 0:
                    __M_writer('            </li>\r\n')
                for i in range(-indent_change_after):
                    __M_writer('            </ul>\r\n')
                    if i + 1 < len(indent_levels):
                        __M_writer('                </li>\r\n')
            if items:
                __M_writer('        <h2>')
                __M_writer(str(messages("Tags")))
                __M_writer('</h2>\r\n')
        if items:
            __M_writer('    <ul class="list-inline">\r\n')
            for text, link in items:
                if text not in hidden_tags:
                    __M_writer('            <li><a class="reference badge" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(text)))
                    __M_writer('</a></li>\r\n')
            __M_writer('    </ul>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bootstrap3/templates/tags.tmpl", "uri": "tags.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "50": 2, "51": 3, "56": 7, "61": 46, "67": 5, "77": 5, "78": 6, "79": 6, "85": 9, "103": 9, "104": 10, "105": 10, "106": 12, "107": 12, "108": 14, "109": 15, "110": 16, "111": 16, "112": 16, "113": 18, "114": 19, "115": 20, "116": 22, "117": 22, "118": 22, "119": 22, "120": 22, "121": 23, "122": 24, "123": 26, "124": 27, "125": 28, "126": 29, "127": 33, "128": 34, "129": 34, "130": 34, "131": 37, "132": 38, "133": 39, "134": 40, "135": 41, "136": 41, "137": 41, "138": 41, "139": 41, "140": 44, "146": 140}}
__M_END_METADATA
"""
