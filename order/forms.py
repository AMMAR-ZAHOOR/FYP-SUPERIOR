from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Rawalpindi', 'Rawalpindi'),
		('Bahawalpur', 'Bahawalpur'),
		('Sargodha', 'Sargodha'),
		('Faisalabad', 'Faisalabad'),
		('Dera Ghazi Khan', 'Dera Ghazi Khan'),
		('Gujranwala','Gujranwala'),
		('Lahore','Lahore'),
		('Multan','Multan'),
		('Sahiwal','Sahiwal'),
		
	)

	DISCRICT_CHOICES = (
		('Attock', 'Attock'), 
		('Bahawalnagar', 'Bahawalnagar'),
		('Bahawalpur', 'Bahawalpur'),
		('Bhakkar', 'Bhakkar'),
		('Chakwal', 'Chakwal'),
		('Chiniot','Chiniot'),
		('Dera Ghazi Khan','Dera Ghazi Khan'),
		('Kasur','Kasur'),
		('Lahore','Lahore'),
		('Okara','Okara'),
		('Sahiwal','Sahiwal'),
		('Sargodha','Sargodha'),
		('Sheikhupura','Sheikhupura'),
		('Sialkot','Sialkot'),
		('Vehari','Vehari'),
		('Toba Tek Singh','Toba Tek Singh'),
		('Nankana Sahib','Nankana Sahib'),
		('Mandi Bahauddin','Mandi Bahauddin'),
		('Layyah','Layyah'),
		('Jhelum','Jhelum'),
		('Hafizabad','Hafizabad'),
		('Gujrat','Gujrat'),
		('Gujranwala','Gujranwala'),
		('Faisalabad','Faisalabad'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Bank Account','Bank Account'),
		('Jazz Cash', 'Jazz Cash'),
		('Eassy Passa','Eassy Passa'),
		('Credit Card','Credit Card')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
