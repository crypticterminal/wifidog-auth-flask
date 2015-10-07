import flask

from app.utils import has_a_role
from flask.ext.security import login_required, roles_accepted
from flask.ext.menu import register_menu

bp = flask.Blueprint('vouchers', __name__, url_prefix='/vouchers', template_folder='templates', static_folder='static')

@bp.route('/')
@login_required
@roles_accepted('super-admin', 'network-admin', 'gateway-admin')
@register_menu(bp, '.vouchers', 'Vouchers', visible_when=has_a_role('super-admin', 'network-admin', 'gateway-admin'), order=30)
def index():
    return flask.render_template('vouchers/index.html')
