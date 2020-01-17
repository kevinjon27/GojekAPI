class BookingEndpointsMixin(object):
    def booking_active(self):
        return self._call_api("/bookings/active", version='v1')
    def booking_completed(self):
        return self._call_api("/bookings/completed", version='v1')