from pyd3charts.globals import JINJA_DEPENDENCIES, BASE_TEMPLATE, SCATTER, MULTISERIES_SCATTER
import jinja2
import webview

def basic_chart(configuration, **kwargs):
    script_name, script_render_variables, key = configuration
    script_render_variables[key] = True
    script_render_variables.update({key: value for key,value in kwargs.items() if value is not None})

    template_loader = jinja2.FileSystemLoader(searchpath=JINJA_DEPENDENCIES)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(BASE_TEMPLATE)

    render_output = template.render(script_render_variables)

    if 'exportpath' in script_render_variables and script_render_variables['exportpath'] is not None:
        open(script_render_variables['exportpath'], 'w+').write(render_output)

    window = webview.create_window('', html=render_output)
    webview.start(debug='debug' in script_render_variables and script_render_variables['debug'] is True)

def scatter_chart(data=None, title='', header='', offset=None, top=None, right=None, bottom=None, left=None, width=None, height=None, radius=None, fill=None, background=None, bodybackground=None, axis=True, tooltip=True, exportpath=None, debug=False):
    render_variables = {key: value for key, value in locals().items() if value is not None}
    basic_chart((SCATTER, render_variables, 'scatter'))

def multiseries_scatter_chart(data=None, series_names=None, title='', header='', offset=None, top=None, right=None, bottom=None, left=None, width=None, height=None, radius=None, fill=None, background=None, bodybackground=None, axis=True, tooltip=True, exportpath=None, debug=False):
    render_variables = {key: value for key, value in locals().items() if value is not None}

    ready_data = [{"name": d[0], "values": d[1]} for d in data]
    series = [d[0] for d in data]

    render_variables['data'] = ready_data
    render_variables['series'] = series

    all_x, all_y = list(zip(*[p for d in data for p in d[1]]))

    max_x = max(all_x)
    min_x = min(all_x)
    max_y = max(all_y)
    min_y = min(all_y)

    render_variables['max_x'] = max_x + (offset if offset is not None else 10)
    render_variables['min_x'] = min_x - (offset if offset is not None else 10)
    render_variables['max_y'] = max_y + (offset if offset is not None else 10)
    render_variables['min_y'] = min_y - (offset if offset is not None else 10)

    basic_chart((MULTISERIES_SCATTER, render_variables, 'multiseries_scatter'))