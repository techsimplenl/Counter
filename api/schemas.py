"""Counter MODULE"""
from flask_marshmallow import Marshmallow
from api.models import Counter
# Create an instance of the Marshmallow class
ma = Marshmallow()

class CounterSchema(ma.Schema):
    """Serializer class for Counter model.
       Serializes Counter instances to JSON format.
    """
    class Meta:
        """Meta class for CounterSchema."""
        model=Counter
        fields=('id','counter')
# Create an instance of CounterSchema for single objects
counter_schema = CounterSchema()
# Create an instance of CounterSchema for multiple objects
counters_schema = CounterSchema(many=True)
