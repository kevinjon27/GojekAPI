class WalletEndpointsMixin(object):
    def wallet_profile(self):
        return self._call_api("wallet/profile")
    
    def wallet_profile_detailed(self):
        return self._call_api("wallet/profile/detailed")