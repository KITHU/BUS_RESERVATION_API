from rest_framework import serializers
from .models.models import Bus, Departure, Passager, Reservation, Route


class DynamicDepthSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Meta.depth = self.context.get('depth', 0)


class PassagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passager
        fields = '__all__'


class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = '__all__'


class DepartureSerializer(serializers.ModelSerializer):
    number=serializers.SerializerMethodField(read_only=True)

    def get_number(self,obj):
        t= obj.bus_id.no_of_seat
        total = set(range(1,t+1))
        booked = Reservation.objects.values_list('seat_no',flat=True).filter(schedule=obj.id)
        # import pdb; pdb.set_trace()
        return total.difference(set(booked))
        
    def __init__(self, *args, **kwargs):
        super(DepartureSerializer, self).__init__(*args, **kwargs)
        try:
            if self.context['request'].method in ['GET', 'RETRIEVE', ]:
                self.fields['route'] = RouteSerializer()
                self.fields['bus_id'] = BusSerializer()
        except KeyError:
            pass
        
    class Meta:
        model = Departure
        fields = '__all__'




class ReservationSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(ReservationSerializer, self).__init__(*args, **kwargs)
        try:
            if self.context['request'].method in ['GET', 'RETRIEVE', ]:
                self.fields['schedule'] = DepartureSerializer()
        except KeyError:
            pass

    class Meta:
        model = Reservation
        fields = '__all__'
