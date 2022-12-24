from config import Configs
from app.utilities import Utilities as Util

if __name__ == "__main__":
    is_prod = False

    configs = Configs(is_prod)

    print(configs.client_id)

    u = Util()
    u.test()
