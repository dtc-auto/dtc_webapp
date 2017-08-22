from django.forms import ModelForm
from datasite.models import  Moment


class MomentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'