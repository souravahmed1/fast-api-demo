from src.router import ping, UserCardRoute



def get_routes():
    return [ ping.router, UserCardRoute.router ]