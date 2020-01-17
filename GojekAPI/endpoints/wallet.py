class WalletEndpointsMixin(object):
    def wallet_profile(self):
        return self._call_api("/wallet/profile")
    
    def wallet_profile_detailed(self):
        return self._call_api("/wallet/profile/detailed")

    def wallet_history(self, page, limit=20):
        data = {
            'page': page,
            'limit': limit
        }
        return self._call_api("/wallet/history", params=data)
    
    def wallet_vouchers(self, page=1, limit=25):
        data = {
            'page': page,
            'limit': limit,
            'new_vouchers_since': '2020-01-10T21:46:21.421Z'
        }
        return self._call_api("/gopoints/v3/wallet/vouchers", params=data)