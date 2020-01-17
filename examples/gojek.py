import json
import os
import argparse

try:
    from GojekAPI import(Client, __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from GojekAPI import(
        Client, __version__ as client_version)


if __name__ == '__main__':

    phone_number = '' #example +6281213031087
    location = '-6.187022998624298,106.74662172641621'


    print('Client version: {0!s}'.format(client_version))

    api = Client(phone_number, location)

    #  Example command:
    #  python examples/example.py
    # result = api.login_with_phone()
    # result = api.verify(otp='7431', login_token='18d41a34-3218-4306-80df-720f4fff6ca3')
    # result = api.wallet_profile()
    # result = api.wallet_profile_detailed()
    # result = api.gofood_consumer_v3_restaurants()
    result = api.gopoints_vouchers()
    print(result)
    

    print('All ok')


