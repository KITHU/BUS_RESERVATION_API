from rest_framework import serializers
from .models.models import Bus, Schedule, Passager, Reservation, Route
from datetime import *


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


class ScheduleSerializer(serializers.ModelSerializer):
    available_seats=serializers.SerializerMethodField(read_only=True)

    def get_available_seats(self,obj):
        t= obj.bus.no_of_seat 
        total = set(range(1,t+1))
        booked = Reservation.objects.values_list('seat_no',flat=True).filter(schedule=obj.id)
        return total.difference(set(booked))
        
    def __init__(self, *args, **kwargs):
        super(ScheduleSerializer, self).__init__(*args, **kwargs)
        try:
            if self.context['request'].method in ['GET', 'RETRIEVE', ]:
                self.fields['route'] = RouteSerializer()
                self.fields['bus'] = BusSerializer()
        except KeyError:
            pass
        
    def create(self, validated_data):
        travel_date = validated_data.get('date_of_travel')
        today_date = date.today()
        if today_date > travel_date:
            raise serializers.ValidationError("Travel date cannot be in the past")
        return super().create(validated_data)  

    class Meta:
        model = Schedule
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(ReservationSerializer, self).__init__(*args, **kwargs)
        try:
            if self.context['request'].method in ['GET', 'RETRIEVE', ]:
                self.fields['schedule'] = ScheduleSerializer()
        except KeyError:
            pass
    
    def create(self, validated_data):
        schedule_id  = validated_data.get("schedule").id
        seat_no = validated_data.get('seat_no')
        no_of_seats = validated_data.get('schedule').bus.no_of_seat

        if seat_no > no_of_seats or seat_no < 1:
            raise serializers.ValidationError("That seat does not exist in this bus")
        if Reservation.objects.all().filter(schedule = schedule_id, seat_no = seat_no).exists():
            raise serializers.ValidationError("seat already booked by other customers")
        
        return super().create(validated_data)

    class Meta:
        model = Reservation
        fields = '__all__'
