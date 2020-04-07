from django.db import models
from django.contrib.auth.models import User


class Dim_Date(models.Model):
    PersianDate = models.CharField(max_length=10)
    SpecialDay = models.IntegerField()
    PersianYear = models.IntegerField()
    PersianYearTitle = models.CharField(max_length=20)
    FiscalYear = models.IntegerField()
    WorkingPeriodYear = models.IntegerField()
    WorkingPeriod = models.IntegerField()
    WorkingPeriodTitle = models.CharField(max_length=20)
    PersianSemester = models.FloatField()
    PersianSemesterTitle = models.CharField(max_length=20)
    PersianQuarter = models.FloatField()
    PersianQuarterTitle = models.CharField(max_length=20)
    PersianMonth = models.FloatField()
    PersianMonthTitle = models.CharField(max_length=20)
    PersianWeekNumberOfYear = models.FloatField()
    PersianWeekNumberOfMonth = models.FloatField()
    PersianDayOfMonth = models.FloatField()
    PersianDayOfYear = models.FloatField()
    PersianWeekDay = models.FloatField()
    PersianWeekDayTitle = models.CharField(max_length=20)

    def __str__(self):
        return str(self.PersianYear) + str(self.PersianMonth) + str(self.PersianDayOfMonth)

    class Meta:
        verbose_name_plural = 'Date'


class WorkSection(models.Model):
    Code = models.CharField(max_length=5)
    Title = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name_plural = 'WorkSection'


class ShiftTypes(models.Model):
    Code = models.CharField(max_length=5)
    Title = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name_plural = 'Shift Types'


class PersonnelTypes(models.Model):
    Code = models.CharField(max_length=5)
    Title = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name_plural = 'Personnel Type'


class Personnel(models.Model):
    PersonnelBaseId = models.IntegerField('PersonnelBaseId in Chargoon')
    FullName = models.CharField(max_length=100)
    WorkSection = models.ForeignKey(WorkSection, on_delete=models.CASCADE)
    YearWorkingPeriod = models.IntegerField()
    RequirementWorkMins_esti = models.IntegerField()
    RequirementWorkMins_real = models.IntegerField()
    PersonnelTypes = models.ForeignKey(PersonnelTypes, on_delete=models.CASCADE)
    EfficiencyRolePoint = models.IntegerField()
    DiffNorm = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.FullName + ' - ' + self.PersonnelTypes

    class Meta:
        verbose_name_plural = 'Personnel'


class Shifts(models.Model):
    Code = models.IntegerField()
    Title = models.CharField(max_length=100)
    Length = models.IntegerField()
    StartTime = models.IntegerField()
    EndTime = models.IntegerField()
    Type = models.CharField('Shift Type Code',max_length=3, null=True, blank=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name_plural = 'Shifts'


class PersonnelRequest(models.Model):
    WorkSection = models.ForeignKey(WorkSection, on_delete=models.CASCADE)
    Personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    YearWorkingPeriod = models.IntegerField()
    Day = models.IntegerField()
    ShiftType = models.ForeignKey(ShiftTypes, on_delete=models.CASCADE)
    Value = models.IntegerField()

    def __str__(self):
        return self.Personnel + ' - ' + self.ShiftType + ' - ' + str(self.Value)

    class Meta:
        verbose_name_plural = 'Personnel Request'


class PersonnelShiftDateAssignments(models.Model):
    WorkSection = models.ForeignKey(WorkSection, on_delete=models.CASCADE)
    PersonnelBaseID = models.IntegerField(null=True) #models.ForeignKey(Personnel, on_delete=models.CASCADE)
    Shift = models.IntegerField(null=True) # = models.ForeignKey(Shifts, on_delete=models.CASCADE)
    YearWorkingPeriod = models.IntegerField()
    Day = models.IntegerField()
    Rank = models.IntegerField()
    Cost = models.FloatField()
    EndTime = models.IntegerField(null=True)
    UsedParentCount = models.IntegerField()

    def __str__(self):
        return self.Personnel + ' - ' + self.Shift + ' -> ' + str(self.YearWorkingPeriod) + str(self.Day)

    class Meta:
        verbose_name_plural = 'Shift Assigned'


class WorkSectionRequirements(models.Model):
    WorkSection = models.ForeignKey(WorkSection, on_delete=models.CASCADE)
    Year = models.IntegerField()
    Month = models.IntegerField()
    DayType = models.IntegerField()
    PersonnelTypeReq = models.ForeignKey(PersonnelTypes, on_delete=models.CASCADE)
    ShiftType = models.ForeignKey(ShiftTypes, on_delete=models.CASCADE)
    ReqMinCount = models.IntegerField()
    ReqMaxCount = models.IntegerField()
    day_diff_typ = models.IntegerField(null=True, blank=True)
    Date = models.IntegerField(null=True, blank=True)
    PersonnelTypeReqCount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.WorkSection + ' - ' + self.PersonnelTypeReq + ' - ' + self.ShiftType + ' - ' + str(
            self.PersonnelTypeReqCount)

    class Meta:
        verbose_name_plural = 'WorkSection Requirements'


class tkp_Logs(models.Model):
    Personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    Date = models.DateField()
    Login = models.IntegerField()
    Logout = models.IntegerField()
    DayDisposition = models.IntegerField()
    YearWorkingPeriodId = models.IntegerField()
    LoginDayDisposition = models.IntegerField()

    def __str__(self):
        return self.Personnel + ' - ' + str(self.Date) + ' - ' + str(self.Login) + ' - ' + str(self.Logout)

    class Meta:
        verbose_name_plural = 'Time Logs'


class ShiftAssignmentPivoted_by_id(models.Model):
    WorkSection = models.IntegerField('واحد', default=0)
    YearWorkingPeriod = models.IntegerField('سال-دوره', default=0)
    Cost = models.DecimalField('هزینه', default=0, max_digits=19, decimal_places=10)
    Rank = models.IntegerField('رتبه', default=0)
    PersonnelBaseId = models.IntegerField('پرسنل', default=0)
    FullName = models.IntegerField('تام پرسنل', default=0)
    PersonnelTypes_id = models.IntegerField('نوع شیفت', default=0)
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
        db_table = 'ShiftAssignmentPivoted'
        managed = False

