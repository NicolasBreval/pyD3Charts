from pyd3charts.globals import SCATTER, JINJA_DEPENDENCIES, BASE_TEMPLATE
import jinja2
import webview

def basic_chart(configuration, **kwargs):
    script_name, script_render_variables = configuration
    script_render_variables['scatter'] = True
    script_render_variables.update({key: value for key,value in kwargs.items() if value is not None})

    template_loader = jinja2.FileSystemLoader(searchpath=JINJA_DEPENDENCIES)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(BASE_TEMPLATE)

    render_output = template.render(script_render_variables)

    if 'exportpath' in script_render_variables and script_render_variables['exportpath'] is not None:
        open(script_render_variables['exportpath'], 'w+').write(render_output)

    window = webview.create_window('', html=render_output)
    webview.start(debug='debug' in script_render_variables and script_render_variables['debug'] is True)

def scatter_chart(data=None, title='', header='', offset=None, top=None, right=None, bottom=None, left=None, width=None, height=None, radius=None, fill=None, axis=None, tooltip=None, exportpath=None, debug=False):
    render_variables = {key: value for key, value in locals().items() if value is not None}
    basic_chart((SCATTER, render_variables))
