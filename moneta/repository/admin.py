# coding=utf-8
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.models import SocialApp, SocialToken
from django.contrib import admin
from django.contrib.sites.models import Site

from moneta.repository.models import Element, Repository


class ElementAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(Site)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)
# admin.site.unregister(EmailConfirmation)

admin.site.register(Element, ElementAdmin)
admin.site.register(Repository)
