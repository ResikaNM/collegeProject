# myapp/forms.py
from django import forms
from collegeApp.models import Department, Course,Students
# class PersonCreationForm(forms.Form):
#     name = forms.CharField(label='Name')
#     dob = forms.DateField(label='DOB')
#     age = forms.IntegerField(label='Age')
#     gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female')])
#     phone_number = forms.CharField(label='Phone Number')
#     mail_id = forms.EmailField(label='Mail ID')
#     address = forms.CharField(label='Address')
#     department = forms.ChoiceField(label='Department', choices=[('Bachelor of Business Management', 'Bachelor of Business Management'), ('Computer Science', 'Computer Science'), ('Biomedical engineering', 'Biomedical engineering'), ('Environmental Studies', 'Environmental Studies'), ('Arts and Humanities', 'Arts and Humanities')])
#     # course = forms.ChoiceField(label='Courses', choices=[('Computer Science', 'Computer Science'), ('Health and Medicine', 'Health and Medicine'), ('Biomedical engineering', 'Biomedical engineering'), ('MBA', 'MBA'), ('Bcom', 'BCom')], required=False)
#     course = forms.ChoiceField(label='Courses', choices=[], required=False)
#     purpose = forms.ChoiceField(label='Purpose', choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
#     materials_provide = forms.MultipleChoiceField(label='Materials Provide', choices=[
#         ('notebook', 'Notebook'),
#         ('pen', 'Pen'),
#         ('exam_papers', 'Exam Papers'),
#         # Add other materials here
#     ], widget=forms.CheckboxSelectMultiple())

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['courses'].queryset = Course.objects.none()
    #
    #     if 'department' in self.data:
    #         try:
    #             department_id = int(self.data.get('department'))
    #             self.fields['courses'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass





class PersonCreationForm(forms.ModelForm):
    # materials_provide = forms.MultipleChoiceField(
    #     label='Materials Provide',
    #     choices=[
    #         ('notebook', 'Notebook'),
    #         ('pen', 'Pen'),
    #         ('exam_papers', 'Exam Papers'),
    #         # Add other materials here
    #     ],
    #     widget=forms.CheckboxSelectMultiple(),  # Use CheckboxSelectMultiple widget
    #     required=False  # Set to True if this field is required
    # )
    class Meta:
        model = Students
        # fields = '__all__'
        exclude =['materials_provide']

    #     widgets = {
    #        'materials_provide': forms.CheckboxSelectMultiple(),  # Rendering the materials_provide field as checkboxes
    # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')