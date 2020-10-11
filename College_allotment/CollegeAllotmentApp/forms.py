from django import forms
from .models import UserData

class UploadForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = [
            'CMPN',
            'INFT',
            'EXTC',
            'ETRX',
            'BIOMED',
            'student_data',
        ]
    
    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['CMPN'].widget.attrs.update({'class' : 'col-sm-3', 'id': 'CMPN'})
        self.fields['INFT'].widget.attrs.update({'class' : 'col-sm-3', 'id': 'INFT'})
        self.fields['EXTC'].widget.attrs.update({'class' : 'col-sm-3', 'id': 'EXTC'})
        self.fields['ETRX'].widget.attrs.update({'class' : 'col-sm-3', 'id': 'ETRX'})
        self.fields['BIOMED'].widget.attrs.update({'class' : 'col-sm-3', 'id':'BIOMED'})
        self.fields['student_data'].widget.attrs.update({'class' : 'col-sm-3'})