import requests
import json


def send_request(url, headers=None, body=None, request_type='GET'):
    """
    Send an HTTP request with optional headers, body, and request type.

    Parameters:
    - url (str): The URL to send the request to.
    - headers (dict, optional): A dictionary of headers to include in the request. Default is None.
    - body (dict or str, optional): The body of the request. Default is None.
    - request_type (str, optional): The HTTP method to use for the request. Default is 'GET'.

    Returns:
    - response (requests.Response): The response object returned by the request.
    """
    
    # Convert the request body to JSON if it's a dictionary
    if isinstance(body, dict):
        body = json.dumps(body)

    print(type(body))
    # Create or update body length header
    headers['Content-Length'] = len(body)

    # Set the appropriate request method
    request_type = request_type.upper()

    if request_type == 'GET':
        response = requests.get(url, headers=headers)
    elif request_type == 'POST':
        response = requests.post(url, headers=headers, data=body)
    elif request_type == 'PUT':
        response = requests.put(url, headers=headers, data=body)
    elif request_type == 'PATCH':
        response = requests.patch(url, headers=headers, data=body)
    elif request_type == 'DELETE':
        response = requests.delete(url, headers=headers, data=body)
    else:
        raise ValueError(f"Invalid request_type: {request_type}")

    return response
