from . import main
from ..utils.res_wrapper import error_response


@main.app_errorhandler(403)
def forbidden(e):
    return error_response(msg="Forbidden", res_code=403)


@main.app_errorhandler(404)
def page_not_found(e):
    return error_response(msg="Page not found", res_code=405)


@main.app_errorhandler(405)
def page_not_found(e):
    return error_response(msg="Method not allowed", res_code=405)


@main.app_errorhandler(500)
def internal_server_error(e):
    return error_response(msg="Internal server error", res_code=500)
