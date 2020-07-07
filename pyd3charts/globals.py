import os

# Files folders
TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
SCRIPTS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')
STYLES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'styles')
EXTERNAL_SCRIPTS_FOLDER = os.path.join(SCRIPTS_FOLDER, 'external')
CHARTS_SCRIPTS_FOLDER = os.path.join(SCRIPTS_FOLDER, 'charts')

JINJA_DEPENDENCIES = [TEMPLATES_FOLDER, EXTERNAL_SCRIPTS_FOLDER, STYLES_FOLDER, CHARTS_SCRIPTS_FOLDER]

# Files names
BASE_TEMPLATE = 'base.html'
SCATTER = 'scatter.js'
MULTISERIES_SCATTER = 'multiseriesscatter.js'