from django.db.models import Model
from django.core import exceptions


def fake_it(model, locale="en-US"):
    if not issubclass(Model):
        raise exceptions.ValidationError("The passed model is not subclass of django.db.models.Model")
    
    pass
