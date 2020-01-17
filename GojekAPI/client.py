# -*- coding: utf-8 -*-
from io import BytesIO
import logging
import gzip
import json
import os
import uuid
import requests

from .constant import Constant

from .endpoints import (WalletEndpointsMixin, GofoodEndpointsMixin)

from .utils import *

# from .endpoints import (
#     ExampleEndpointsMixin
# )

logger = logging.getLogger(__name__)


class Client(GofoodEndpointsMixin, WalletEndpointsMixin, object):
    def __init__(self, phone_number, location, GODataPath=None, **kwargs):
        """
        :param kwargs: See below
        :Keyword Arguments:
            - **timeout**: Timeout interval in seconds. Default: 15
            - **api_url**: Override the default api url base
        :return:
        """

        self.phone_number = None
        self.customer_id = None
        self.location = None
        self.timeout = kwargs.pop('timeout', 15)
        self.logger = logger
        self.settings = None
        self.uuid = None  # // UUID
        self.isLoggedIn = False
        self.token = None  # // _csrftoken
        self.GODataPath = None
        self.customPath = False

        if GODataPath is not None:
            self.GODataPath = GODataPath
            self.customPath = True
        else:
            self.GODataPath = os.path.join(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data'),
                phone_number,
                ''
            )
            if not os.path.isdir(self.GODataPath):
                os.mkdir(self.GODataPath, 0o777)
        
        self.checkSettings(phone_number)
        self.setUser(phone_number, location)
    

        super(Client, self).__init__()
    

    def setUser(self, phone_number, location):
        """
        Set the user. Manage multiple accounts.
        :type phone_number: str
        :param phone_number: Your Instagram phone_number.
        :
        """
        self.phone_number = phone_number
        self.location = location

        self.checkSettings(phone_number)

        if os.path.isfile(self.GODataPath + 'settings-'+ self.phone_number + '.dat') and \
                (self.settings.get('customer_id') != None)  and \
                (self.settings.get('access_token') != None):
            self.isLoggedIn = True
            self.customer_id = self.settings.get('customer_id')
            self.token = self.settings.get('access_token')
            self.uuid = self.settings.get('uuid')
        else:
            self.isLoggedIn = False

    def login_with_phone(self, force=False):
        response = None
        self.settings.set('location', str(self.location))
        if (not self.isLoggedIn) or force:
            self.uuid = uuid.uuid4()
            self.settings.set('uuid', str(self.uuid))

            data = {
                'phone': self.phone_number
            }

            response = self._call_api('/customers/login_with_phone', params=data, version="v4", method="POST")
            return response
        else:
            return 'user has been logged in.'



    def verify(self, otp, login_token):
        if (not self.isLoggedIn):
            data = {
                'client_name': 'gojek:cons:ios',
                'grant_type': 'otp',
                'scopes': 'gojek:customer:transaction gojek:customer:readonly',
                'data': {
                    'otp': otp,
                    'otp_token': login_token
                },
                'client_secret': Constant.CLIENT_SECRET
            }

            response = self._call_api('/customers/login/verify', params=data, version="v4", method="POST")

            if response['success'] == True:
                customer = response['data']['customer']
            
                self.isLoggedIn = True
                self.customer_id = customer['id']
                self.settings.set('customer_id', self.customer_id)
                self.settings.set('access_token', response['data']['access_token'])
                return response
            else:
                return response['errors']
            
        else:
            return 'user has been logged in.'
    

    def checkSettings(self, phone_number):
        if not self.customPath:
            self.GODataPath = os.path.join(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data'),
                phone_number,
                ''
            )

        if not os.path.isdir(self.GODataPath): os.mkdir(self.GODataPath, 0o777)

        self.settings = Settings(
            os.path.join(self.GODataPath, 'settings-' + phone_number + '.dat')
        )
    @property
    def default_headers(self):
        return {
            'X-AppId': Constant.APP_ID,
            'X-PhoneModel': Constant.PHONE_MODEL,
            'User-Agent': Constant.USER_AGENT,
            'X-UniqueId': self.settings.get('uuid'),
            'X-Location': self.settings.get('location'),
            'Accept-Language': 'id-ID', #en-ID
            'X-User-Locale': 'id_ID', #en-ID
            'X-Platform': 'iOS',
            'X-Location-Accuracy': Constant.LOCATION_ACCURACY,
            'X-AppVersion': Constant.APP_VERSION
        }

    def _call_api(self, endpoint, params=None, return_response=False, version="", method="GET"):
        """
        Calls the private api.
        :param endpoint: endpoint path that should end with '/', example 'discover/explore/'
        :param params: POST parameters
        :param query: GET url query parameters
        :param return_response: return the response instead of the parsed json object
        :param version: for the versioned api base url. Default 'v1'.
        :param method
        :return:
        """
        url = "{0}{1}".format(Constant.API_BASE_URL.format(version=version), endpoint)


        headers = self.default_headers
        response = None

        if (self.settings.get('access_token')):
            headers['Authorization'] = 'Bearer ' + self.settings.get('access_token')

        if (method == 'POST'):
            response = requests.post(url, json=params, headers=headers)
        else:
            response = requests.get(url, params=params, headers=headers)



        json_response = response.json()

        print("url: " + url)
        return json_response