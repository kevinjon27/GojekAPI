class GopointsEndpointsMixin(object):
    def gopoints_vouchers(self, page=1, limit=25):
        data = {
            'page': page,
            'limit': limit,
            'new_vouchers_since': '2020-01-10T21:46:21.421Z'
        }
        return self._call_api("/gopoints/v3/wallet/vouchers", params=data)