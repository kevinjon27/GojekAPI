class CustomerEndpointsMixin(object):
    def customer_profile(self):
        return self._call_api("/customers/active_booking", version='v1')