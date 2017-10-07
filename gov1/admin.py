# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SignUp,Complaint,Suggestion,Birth,Water,Voter,Death,Electricity,Mobile

admin.site.register(SignUp)
admin.site.register(Complaint)
admin.site.register(Suggestion)
admin.site.register(Birth)
admin.site.register(Water)
admin.site.register(Voter)
admin.site.register(Death)
admin.site.register(Electricity)
admin.site.register(Mobile)


