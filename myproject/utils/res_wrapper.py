from flask import jsonify, Response


def success_response(msg="", data={}, res_code=200) -> Response:
    """
    Membungkus respons sukses dengan format JSON
    """
    return jsonify(
        {
            "data": data,
            "message": msg,
            "status": "Success"
        }
    ), res_code


def error_response(msg="", data={}, res_code=400) -> Response:
    """
    Membungkus respons error dengan format JSON
    """
    return jsonify(
        {
            "data": data,
            "message": msg,
            "status": "Error"
        }
    ), res_code
