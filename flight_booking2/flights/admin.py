from django.contrib import admin
import flights.models as models


class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'flight_id',
        'departure_date',
        'departure_time',
        'available_seats',
    )
    list_filter = (
        'departure_date',
        'flight_id',
        'departure_time',
    )
    ordering = ('-departure_date',)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight_number',
                    'departure_date', 'departure_time')
    list_filter = ('user', 'flight', 'id')
    ordering = ('user',)

    def flight_number(self, obj):
        return obj.flight.flight_id

    def departure_date(self, obj):
        return obj.flight.departure_date

    def departure_time(self, obj):
        return obj.flight.departure_time


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Flight, FlightAdmin)
_register(models.Booking, BookingAdmin)
