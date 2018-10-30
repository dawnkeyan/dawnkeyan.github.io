# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1540910612.0879161
_enable_loop = True
_template_filename = 'themes/bootstrap3/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content', 'extra_head', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        gallery_path = _import_ns.get('gallery_path', context.get('gallery_path', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        def content():
            return render_content(context)
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\r\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\r\n')
        if post:
            __M_writer('    <p>\r\n        ')
            __M_writer(str(post.text()))
            __M_writer('\r\n    </p>\r\n')
        if folders:
            __M_writer('    <ul>\r\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i>&nbsp;')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a></li>\r\n')
            __M_writer('    </ul>\r\n')
        __M_writer('\r\n<div id="gallery_container"></div>\r\n')
        if photo_array:
            __M_writer('<noscript>\r\n<ul class="thumbnails">\r\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('">\r\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" /></a>\r\n')
            __M_writer('</ul>\r\n</noscript>\r\n')
        if site_has_comments and enable_comments:
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        gallery_path = _import_ns.get('gallery_path', context.get('gallery_path', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\r\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\r\n<style type="text/css">\r\n    #gallery_container {\r\n        position: relative;\r\n    }\r\n    .image-block {\r\n        position: absolute;\r\n    }\r\n</style>\r\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang:
                    __M_writer('             <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(_link('gallery', gallery_path, langname)))
                    __M_writer('">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_js():
            return render_extra_js(context)
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n<script src="/assets/js/justified-layout.min.js"></script>\r\n<script src="/assets/js/gallery.min.js"></script>\r\n<script>\r\nvar jsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\r\nvar thumbnailSize = ')
        __M_writer(str(thumbnail_size))
        __M_writer(";\r\nrenderGallery(jsonContent, thumbnailSize);\r\nwindow.addEventListener('resize', renderGallery);\r\n</script>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bootstrap3/templates/gallery.tmpl", "uri": "gallery.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "32": 0, "65": 2, "66": 3, "67": 4, "72": 5, "77": 39, "82": 59, "87": 70, "93": 5, "106": 7, "124": 7, "125": 8, "126": 8, "127": 9, "128": 10, "129": 10, "130": 10, "131": 12, "132": 13, "133": 14, "134": 14, "135": 17, "136": 18, "137": 19, "138": 20, "139": 20, "140": 20, "141": 20, "142": 20, "143": 22, "144": 24, "145": 26, "146": 27, "147": 29, "148": 30, "149": 30, "150": 30, "151": 30, "152": 30, "153": 31, "154": 31, "155": 31, "156": 31, "157": 33, "158": 36, "159": 37, "160": 37, "166": 41, "180": 41, "181": 42, "182": 42, "183": 52, "184": 53, "185": 54, "186": 55, "187": 55, "188": 55, "189": 55, "190": 55, "196": 61, "206": 61, "207": 65, "208": 65, "209": 66, "210": 66, "216": 210}}
__M_END_METADATA
"""
