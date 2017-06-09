def return_response(response):
    try:
        return response.json()
    except:
        return response

