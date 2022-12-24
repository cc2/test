def init(is_prod):
    global client_id
    if is_prod:
        client_id = 100
    else:
        client_id = 300
