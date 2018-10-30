# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1540910612.196922
_enable_loop = True
_template_filename = 'd:/workspace/python/nikola/nikola/data/themes/base/templates/comments_helper_facebook.tmpl'
_template_uri = 'comments_helper_facebook.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="fb-root"></div>\r\n<script>\r\n  window.fbAsyncInit = function() {\r\n    // init the FB JS SDK\r\n    FB.init({\r\n      appId      : \'')
        __M_writer(str(comment_system_id))
        __M_writer('\',\r\n      status     : true,\r\n      xfbml      : true\r\n    });\r\n\r\n  };\r\n\r\n  // Load the SDK asynchronously\r\n  (function(d, s, id){\r\n     var js, fjs = d.getElementsByTagName(s)[0];\r\n     if (d.getElementById(id)) {return;}\r\n     js = d.createElement(s); js.id = id;\r\n     js.src = "https://connect.facebook.net/en_US/all.js";\r\n     fjs.parentNode.insertBefore(js, fjs);\r\n   }(document, \'script\', \'facebook-jssdk\'));\r\n</script>\r\n\r\n<div class="fb-comments" data-href="')
        __M_writer(str(url))
        __M_writer('" data-width="470"></div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\r\n<span class="fb-comments-count" data-url="')
        __M_writer(str(link))
        __M_writer('">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="fb-root"></div>\r\n<script>\r\n    // thank lxml for this\r\n    $(\'.fb-comments-count\').each(function(i, obj) {\r\n        var url = obj.attributes[\'data-url\'].value;\r\n        // change here if you dislike the default way of displaying\r\n        // this\r\n        obj.innerHTML = \'<fb:comments-count href="\' + url + \'"></fb:comments-count> comments\';\r\n    });\r\n\r\n  window.fbAsyncInit = function() {\r\n    // init the FB JS SDK\r\n    FB.init({\r\n      appId      : \'')
        __M_writer(str(comment_system_id))
        __M_writer('\',\r\n      status     : true,\r\n      xfbml      : true\r\n    });\r\n\r\n  };\r\n\r\n  // Load the SDK asynchronously\r\n  (function(d, s, id){\r\n     var js, fjs = d.getElementsByTagName(s)[0];\r\n     if (d.getElementById(id)) {return;}\r\n     js = d.createElement(s); js.id = id;\r\n     js.src = "https://connect.facebook.net/en_US/all.js";\r\n     fjs.parentNode.insertBefore(js, fjs);\r\n   }(document, \'script\', \'facebook-jssdk\'));\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "d:/workspace/python/nikola/nikola/data/themes/base/templates/comments_helper_facebook.tmpl", "uri": "comments_helper_facebook.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 26, "22": 30, "23": 62, "29": 2, "34": 2, "35": 8, "36": 8, "37": 25, "38": 25, "44": 28, "48": 28, "49": 29, "50": 29, "56": 32, "61": 32, "62": 46, "63": 46, "69": 63}}
__M_END_METADATA
"""
