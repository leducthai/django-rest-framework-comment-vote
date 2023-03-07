from rest_framework import serializers
from .models import comment
from .validators import no_fuck_in_comment

class comment_serializer(serializers.ModelSerializer):
    comment = serializers.CharField(source='body' ,validators=[no_fuck_in_comment])
    class Meta:
        model = comment
        fields = [
            'pd_id',
            'user_id',
            'comment'
        ]


    