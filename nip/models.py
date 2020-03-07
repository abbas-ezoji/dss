from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ShiftAssignmentPivoted_by_id(models.Model):
    # id = models.IntegerField(primary_key=True)
    WorkSectionId = models.IntegerField('واحد', default=0)
    YearWorkingPeriod = models.IntegerField('سال-دوره', default=0)
    Cost = models.DecimalField('هزینه', default=0, max_digits=19, decimal_places=10)
    Rank = models.IntegerField('رتبه', default=0)
    PersonnelBaseId = models.IntegerField('پرسنل', default=0)
    FullName = models.IntegerField('تام پرسنل', default=0)
    TypeId = models.IntegerField('نوع شیفت', default=0)
    D01 = models.IntegerField('ر01', default=0)
    D02 = models.IntegerField('ر02', default=0)
    D03 = models.IntegerField('ر03', default=0)
    D04 = models.IntegerField('ر04', default=0)
    D05 = models.IntegerField('ر05', default=0)
    D06 = models.IntegerField('ر06', default=0)
    D07 = models.IntegerField('ر07', default=0)
    D08 = models.IntegerField('ر08', default=0)
    D09 = models.IntegerField('ر09', default=0)
    D10 = models.IntegerField('ر10', default=0)
    D11 = models.IntegerField('ر11', default=0)
    D12 = models.IntegerField('ر12', default=0)
    D13 = models.IntegerField('ر13', default=0)
    D14 = models.IntegerField('ر14', default=0)
    D15 = models.IntegerField('ر15', default=0)
    D16 = models.IntegerField('ر16', default=0)
    D17 = models.IntegerField('ر17', default=0)
    D18 = models.IntegerField('ر18', default=0)
    D19 = models.IntegerField('ر19', default=0)
    D20 = models.IntegerField('ر20', default=0)
    D21 = models.IntegerField('ر21', default=0)
    D22 = models.IntegerField('ر22', default=0)
    D23 = models.IntegerField('ر23', default=0)
    D24 = models.IntegerField('ر24', default=0)
    D25 = models.IntegerField('ر25', default=0)
    D26 = models.IntegerField('ر26', default=0)
    D27 = models.IntegerField('ر27', default=0)
    D28 = models.IntegerField('ر28', default=0)
    D29 = models.IntegerField('ر29', default=0)
    D30 = models.IntegerField('ر30', default=0)
    D31 = models.IntegerField('ر31', default=0)

    def __str__(self):
        return self.WorkSectionId

    class Meta:
        verbose_name_plural = 'شیفت اختصاص داده شده'
        db_table = '[VW].[ShiftAssignmentPivoted]'
        managed = False