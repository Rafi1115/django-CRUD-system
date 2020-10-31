from django import forms
from tinymce.widgets import TinyMCE
from tinymce import TinyMCE
from .models import BookModel
from .widgets import XDSoftDateTimePickerInput, BootstrapDateTimePickerInput, FengyuanChenDatePickerInput





class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class XDSoftEventForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=XDSoftDateTimePickerInput())
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={
            'required': False, 'cols': 30, 'rows': 25
            }
        )
    )
    class Meta:
        model = BookModel
        exclude = ['ouruser']
        fields = (
            'name', 'email', 'phone', 'pickup', 'content',
            'destination', 'date'
        )
        widgets = { 
            'name' : forms.TextInput
                        (attrs={'placeholder': 'Your Name'}), 
            'email' : forms.TextInput
                        (attrs={'placeholder': 'Ex: example@gamil/yahoo.com'}), 
            'phone' : forms.TextInput
                        (attrs={'placeholder': 'Contact Number'}), 
            'pickup' : forms.TextInput
                        (attrs={'placeholder': 'Pickup Location'}), 
        }

class BootstrapEventForm(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=BootstrapDateTimePickerInput())

    class Meta:
        model = BookModel
        fields = (
            'name', 'email', 'phone', 'pickup',
            'destination', 'date'
        )



class FengyuanChenEventForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'], widget=FengyuanChenDatePickerInput())

    class Meta:
        model = BookModel
        fields = (
            'name', 'email', 'phone', 'pickup',
            'destination', 'date'
        )
