# -*- coding: utf-8 -*-
from django import forms


class ChargeForm(forms.Form):
    order_no = forms.CharField(max_length=32)
    amount = forms.IntegerField(min_value=1)
