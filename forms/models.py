from django.db import models
from django.utils import timezone

# Create your models here.
# for BogieForm, BogieDetails, BogieChecksheet, BMBCChecksheet

class BogieForm(models.Model):
    formNumber = models.CharField(max_length=50)
    inspection_by = models.CharField(max_length=100, null=False, blank=False)
    inspection_date = models.DateField(default=timezone.now) 

    def __str__(self):
        return self.formNumber
    
class BogieDetails(models.Model):
    form = models.OneToOneField(BogieForm, on_delete=models.CASCADE, related_name='bogieDetails')
    bogieNo = models.CharField(max_length=50)
    dateOfIOH = models.DateField()
    deficitComponents = models.CharField(max_length=255)
    incomingDivAndDate = models.CharField(max_length=100)
    makerYearBuilt = models.CharField(max_length=100)

class BogieChecksheet(models.Model):
    form = models.OneToOneField(BogieForm, on_delete=models.CASCADE, related_name='bogieChecksheet')
    axleGuide = models.CharField(max_length=50)
    bogieFrameCondition = models.CharField(max_length=50)
    bolster = models.CharField(max_length=50)
    bolsterSuspensionBracket = models.CharField(max_length=50)
    lowerSpringSeat = models.CharField(max_length=50)

class BMBCChecksheet(models.Model):
    CONDITION_CHOICES = [
    ('GOOD', 'Good'),
    ('WORN_OUT', 'Worn Out'),
    ('DAMAGED', 'Damaged'),
    ('OTHER', 'Other'),
]
    form = models.OneToOneField(BogieForm, on_delete=models.CASCADE, related_name='bmbcChecksheet')
    adjustingTube = models.CharField(max_length=50,choices=CONDITION_CHOICES, default='GOOD')
    cylinderBody = models.CharField(max_length=50,choices=CONDITION_CHOICES, default='GOOD')
    pistonTrunnion = models.CharField(max_length=50,choices=CONDITION_CHOICES, default='GOOD')
    plungerSpring = models.CharField(max_length=50,choices=CONDITION_CHOICES, default='GOOD')


# for WheelForm, WheelFields
class WheelForm(models.Model):
    formNumber = models.CharField(max_length=50)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()

    def __str__(self):
        return self.formNumber
    
class WheelFields(models.Model):
    form = models.OneToOneField(WheelForm, on_delete=models.CASCADE, related_name='fields')
    treadDiameterNew = models.CharField(max_length=50)
    lastShopIssueSize = models.CharField(max_length=50)
    condemningDia = models.CharField(max_length=50)
    wheelGauge = models.CharField(max_length=50)
    variationSameAxle = models.CharField(max_length=50)
    variationSameBogie = models.CharField(max_length=50)
    variationSameCoach = models.CharField(max_length=50)
    wheelProfile = models.CharField(max_length=100)
    intermediateWWP = models.CharField(max_length=100)
    bearingSeatDiameter = models.CharField(max_length=100)
    rollerBearingOuterDia = models.CharField(max_length=100)
    rollerBearingBoreDia = models.CharField(max_length=100)
    rollerBearingWidth = models.CharField(max_length=100)
    axleBoxHousingBoreDia = models.CharField(max_length=100)
    wheelDiscWidth = models.CharField(max_length=100)