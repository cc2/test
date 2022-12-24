import config
from app.utilities import Utilities as Util

if __name__ == "__main__":
    is_prod = False

    config.init(is_prod)

    print(config.client_id)

    u = Util()
    u.test()
