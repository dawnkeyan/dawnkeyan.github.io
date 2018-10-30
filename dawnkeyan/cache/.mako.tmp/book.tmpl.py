# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1540910612.4589372
_enable_loop = True
_template_filename = 'templates/book.tmpl'
_template_uri = 'book.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        parent = context.get('parent', UNDEFINED)
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer("\r\n    <link href='https://fonts.googleapis.com/css?family=Gentium+Book+Basic' rel='stylesheet' type='text/css'>\r\n    <style>\r\n        .smallcaps {\r\n            font-variant: small-caps;\r\n        }\r\n        .chapter {\r\n            width: 100%;\r\n            padding: 10px;\r\n            -webkit-column-gap: 40px;\r\n               -moz-column-gap: 40px;\r\n                    column-gap: 40px;\r\n            -webkit-column-width: 400px;\r\n               -moz-column-width: 400px;\r\n                    column-width: 400px;\r\n            -webkit-column-count: 2;\r\n               -moz-column-count: 2;\r\n                    column-count: 2;\r\n            -webkit-column-rule: 1px solid #ddd;\r\n               -moz-column-rule: 1px solid #ddd;\r\n                    column-rule: 1px solid #ddd;\r\n            height: 90vh;\r\n            font-family: 'Gentium Book Basic', serif;\r\n            color: #2d2e2e;\r\n            font-weight: 500;\r\n        }\r\n        div.frame {\r\n            overflow: hidden;\r\n            padding: 0;\r\n            margin: 0;\r\n        }\r\n        div.scrolling-cont {\r\n            overflow-x: scroll;\r\n            padding: 0;\r\n            margin: 0;\r\n        }\r\n        h1, h2, h3, h4 {\r\n            text-align: center;\r\n            width: 100%;\r\n            font-family: 'Gentium Book Basic', serif;\r\n            font-size: 120%;\r\n            font-weight: 900;\r\n        }\r\n        h1 {\r\n            font-size: 150%;\r\n        }\r\n        .subtitle {\r\n            text-align: center;\r\n            width: 100%;\r\n        }\r\n        .bookfig {\r\n            width: 100%;\r\n            height: auto;\r\n            max-width: 100%;\r\n            max-height: 100%;\r\n        }\r\n        div.figure {\r\n            height: 88vh;\r\n            margin: 0;\r\n        }\r\n        div.topic {\r\n            margin: 0;\r\n        }\r\n        div.section > p {\r\n            text-indent: 1em;\r\n            margin-bottom: 0;\r\n            text-align: justify;\r\n        }\r\n    </style>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<article class="storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\r\n    <div class="frame">\r\n    <div class="scrolling-cont" id="scrolling-cont" name="scrolling-cont">\r\n    <div class="e-content entry-content chapter" itemprop="articleBody text">\r\n    <h1>')
        __M_writer(str(post.title()))
        __M_writer('</h1>\r\n    ')
        __M_writer(str(post.text()))
        __M_writer('\r\n    </div>\r\n    </div>\r\n    </div>\r\n</article>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/Flowtype.js/1.1.0/flowtype.min.js"></script>\r\n    <script>\r\n        $(\'#scrolling-cont\').flowtype({\r\n            minimum: 500,\r\n            maximum: 1200,\r\n            minFont: 20,\r\n            maxFont: 40,\r\n            fontRatio: 50\r\n        });\r\n        $(document).ready(function() {\r\n            var elem = $(\'#scrolling-cont\');\r\n            elem.click(function(event) {\r\n                var x1 = elem.position().left;\r\n                var pw = elem.width() + 20;\r\n                var x2 = event.pageX;\r\n                if (x2 - x1 < pw / 2) {\r\n                    pw = -pw;\r\n                }\r\n                elem.animate({\r\n                    scrollLeft: \'+=\' + pw\r\n                }, 500)\r\n            });\r\n        });\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/book.tmpl", "uri": "book.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "48": 2, "49": 3, "50": 4, "51": 5, "56": 77, "61": 90, "66": 117, "72": 7, "79": 7, "80": 8, "81": 8, "87": 79, "94": 79, "95": 84, "96": 84, "97": 85, "98": 85, "104": 92, "110": 92, "116": 110}}
__M_END_METADATA
"""
