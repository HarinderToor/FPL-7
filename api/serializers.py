from rest_framework import serializers

class PlayerSerializer(serializers.Serializer):
    magnificence = serializers.SerializerMethodField()
    team = serializers.CharField(max_length=100)
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return f"{obj['first_name']} {obj['second_name']}"

    def get_magnificence(self, obj):
        return obj['goals_scored'] + obj['assists']

class Best7TeamSerializer(serializers.Serializer):
    goalkeeper = PlayerSerializer()
    defenders = PlayerSerializer(many=True)
    midfielders = PlayerSerializer(many=True)
    forwards = PlayerSerializer(many=True)
