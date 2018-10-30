# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1540910612.3599315
_enable_loop = True
_template_filename = 'd:/workspace/python/nikola/nikola/data/themes/base/templates/math_helper.tmpl'
_template_uri = 'math_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['math_scripts', 'math_styles', 'math_scripts_ifpost', 'math_scripts_ifposts', 'math_styles_ifpost', 'math_styles_ifposts']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        katex_auto_render = context.get('katex_auto_render', UNDEFINED)
        use_katex = context.get('use_katex', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if use_katex:
            __M_writer('        <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.js" integrity="sha384-/y1Nn9+QQAipbNQWU65krzJralCnuOasHncUFXGkdwntGeSvQicrYkiUBwsgUqc1" crossorigin="anonymous"></script>\r\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/contrib/auto-render.min.js" integrity="sha256-ExtbCSBuYA7kq1Pz362ibde9nnsHYPt6JxuxYeZbU+c=" crossorigin="anonymous"></script>\r\n')
            if katex_auto_render:
                __M_writer('            <script>\r\n                renderMathInElement(document.body,\r\n                    {\r\n                        ')
                __M_writer(str(katex_auto_render))
                __M_writer('\r\n                    }\r\n                );\r\n            </script>\r\n')
            else:
                __M_writer('            <script>\r\n                renderMathInElement(document.body,\r\n                    {\r\n                        delimiters: [\r\n                            {left: "$$", right: "$$", display: true},\r\n                            {left: "\\\\[", right: "\\\\]", display: true},\r\n                            {left: "\\\\begin{equation*}", right: "\\\\end{equation*}", display: true},\r\n                            {left: "\\\\(", right: "\\\\)", display: false}\r\n                        ]\r\n                    }\r\n                );\r\n            </script>\r\n')
        else:
            __M_writer('        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML" integrity="sha256-SDRP1VVYu+tgAGKhddBSl5+ezofHKZeI+OzxakbIe/Y=" crossorigin="anonymous"></script>\r\n')
            if mathjax_config:
                __M_writer('        ')
                __M_writer(str(mathjax_config))
                __M_writer('\r\n')
            else:
                __M_writer('        <script type="text/x-mathjax-config">\r\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\r\n        </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_katex = context.get('use_katex', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if use_katex:
            __M_writer('        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.css" integrity="sha384-wITovz90syo1dJWVh32uuETPVEtGigN07tkttEqPv+uR2SE/mbQcG7ATL28aI9H0" crossorigin="anonymous">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts_ifpost(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_scripts():
            return render_math_scripts(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if post.has_math:
            __M_writer('        ')
            __M_writer(str(math_scripts()))
            __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_scripts_ifposts(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        any = context.get('any', UNDEFINED)
        def math_scripts():
            return render_math_scripts(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if any(post.has_math for post in posts):
            __M_writer('        ')
            __M_writer(str(math_scripts()))
            __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles_ifpost(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def math_styles():
            return render_math_styles(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if post.has_math:
            __M_writer('        ')
            __M_writer(str(math_styles()))
            __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_math_styles_ifposts(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        any = context.get('any', UNDEFINED)
        def math_styles():
            return render_math_styles(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if any(post.has_math for post in posts):
            __M_writer('        ')
            __M_writer(str(math_styles()))
            __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "d:/workspace/python/nikola/nikola/data/themes/base/templates/math_helper.tmpl", "uri": "math_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 39, "22": 45, "23": 51, "24": 57, "25": 63, "26": 69, "32": 2, "39": 2, "40": 3, "41": 4, "42": 6, "43": 7, "44": 10, "45": 10, "46": 14, "47": 15, "48": 28, "49": 30, "50": 31, "51": 32, "52": 32, "53": 32, "54": 33, "55": 34, "61": 41, "66": 41, "67": 42, "68": 43, "74": 47, "80": 47, "81": 48, "82": 49, "83": 49, "84": 49, "90": 53, "97": 53, "98": 54, "99": 55, "100": 55, "101": 55, "107": 59, "113": 59, "114": 60, "115": 61, "116": 61, "117": 61, "123": 65, "130": 65, "131": 66, "132": 67, "133": 67, "134": 67, "140": 134}}
__M_END_METADATA
"""
