from django.contrib import admin
from leads.models import Lead
from django.db import models
from django.utils.html import format_html
import csv
from django.http import HttpResponse, HttpResponseRedirect

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, delimiter=';')

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class LeadFormAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('id','subject', 'email', 'message_short', 'notice', 'created_at', 'answer_custom', 'is_email_answer_send', 'updated_at', 'answered_by_admin', 'send_answer')
    list_display_links = ('id', 'subject')
    search_fields = ('email', 'subject')
    list_filter = ('is_email_answer_send',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'answer', 'answered_by', 'is_email_answer_send')
    list_editable = ('notice',)
    actions = ('export_as_csv',)


    # Используем w3schhol tooltip https://www.w3schools.com/css/tryit.asp?filename=trycss_tooltip
    def message_short(self, obj):
        message = obj.message[:20] + '...'
        return format_html(
            """
            <div class="tooltip">{0}
                <span class="tooltiptext">{1}</span>
            </div>
            """.format(message, obj.message)
        ) 
    
    def answered_by_admin(self, obj):
        if obj.answered_by is not None:
            return obj.answered_by.get_full_name()
        else:
            return '-'
    
    def answer_custom(self, obj):
        if obj.is_email_answer_send:
            if obj.answer:
                return format_html(
                    """<textarea name="form-{0}-answer" cols="40" rows="10" class="vLargeTextField" id="id_form-{0}-answer" readonly>{1}</textarea>""".format(obj.id, obj.answer)
                )
        else:
            return format_html(
                    """<textarea name="form-{0}-answer" cols="40" rows="10" class="vLargeTextField" id="id_form-{0}-answer" value=""></textarea>""".format(obj.id)
                )
    
    def send_answer(self, obj):
        if obj.is_email_answer_send:
            send_answer_button = """"""
        else:
            send_answer_button = """
            <a type="button" class="button default"  href="#" onclick="sendAnswer({0});">Отправить ответ</a>

            """.format(obj.id)
        return format_html(send_answer_button)

admin.site.register(Lead, LeadFormAdmin)


