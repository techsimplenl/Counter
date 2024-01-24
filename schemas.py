"""Counter MODULE"""
from flask_marshmallow import Marshmallow
from models import Counter

ma = Marshmallow()

class CounterSchema(ma.Schema):
    """Serializer class"""
    class Meta:
        """Meta class"""
        model=Counter
        fields=('id','counter')
counter_schema = CounterSchema()
counters_schema = CounterSchema(many=True)
