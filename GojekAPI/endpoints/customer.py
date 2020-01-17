class CustomerEndpointsMixin(object):
    def customer_active_bookings(self):
        return self._call_api("/customers/active_bookings", version='v1')