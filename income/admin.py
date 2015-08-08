from django.contrib import admin

from income.models.records import IncomeRecord
from income.models.predict import IncomePredict


class IncomeRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'number')

    list_editable = ('number',)

    ordering = ('-timestamp',)

    def date(self, obj):
        return obj.timestamp.strftime("%Y/%m")

admin.site.register(IncomeRecord, IncomeRecordAdmin)
