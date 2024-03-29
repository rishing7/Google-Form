def build_response_dict(response_type, response_text, id=None, response_data=None):

    """
    Helper function to create a response dict
    :param response_type: Request method type
    :param response_text: Response message text
    :param id: id to be appended to post request
    :param response_data: response payload to be outputted
    :return: dictionary consisting of response
    """
    response_dict = dict()
    response_dict["message"] = response_text
    if response_type == "POST":
        if id:
            response_dict.update(id)
        response_dict["status_code"] = 201
    elif response_type == "PUT":
        response_dict["status_code"] = 202
    elif response_type == "DELETE":
        response_dict["status_code"] = 204
    else:
        response_dict["status_code"] = 200
        if response_data:
            response_dict["payload"] = response_data
    return response_dict