from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class User(BaseModel):
    email = models.CharField(verbose_name='Email id', max_length=455, unique=True)
    password = models.CharField(verbose_name='Password', max_length=456, blank=True, null=True)
    user_name = models.CharField(verbose_name='Username', max_length=455, unique=True)

    first_name = models.CharField(verbose_name='First Name', max_length=455, blank=True, null=True)
    last_name = models.CharField(verbose_name='Second Name', max_length=455, blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
    gender = models.CharField(verbose_name='Gender', max_length=10, blank=True, null=True)
    contact_no = models.PositiveBigIntegerField(verbose_name='Contact No', blank=True, null=True)
    last_login = models.DateTimeField(verbose_name='Last Login', blank=True, null=True)
    otp = models.IntegerField(verbose_name='OTP', blank=True, null=True)
    is_email_verified = models.BooleanField(verbose_name='Is Email verified', default=False)
    # todo profile photo

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.user_name}"

class State(BaseModel):
    name = models.CharField(verbose_name='State', max_length=456)

    class Meta:
        db_table = "states"
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return f"{self.name}"

class Odyssey(BaseModel):
    organiser = models.ForeignKey(User, verbose_name="Organiser", related_name='odysseies_organiser', related_query_name='odyssey_organiser', on_delete=models.CASCADE)
    user = models.ManyToManyField(User, verbose_name="Travellers", related_name="odysseies", related_query_name="odyssey")
    start_date = models.DateTimeField(verbose_name='Odyssey Start Date', blank=True, null=True)
    end_date = models.DateTimeField(verbose_name='Odyssey End Date', blank=True, null=True)
    from_place = models.ForeignKey(State, verbose_name='Odyssey\'s start place', related_name='odysseies_from_places',
                                   related_query_name='odyssey_from_place', on_delete=models.CASCADE)
    destination_place = models.ForeignKey(State, verbose_name='Odyssey\'s end place',
                                          related_name='odysseies_to_places', related_query_name='odyssey_to_place',
                                          on_delete=models.CASCADE)
    is_private = models.BooleanField(verbose_name='Is Private', default=False)
    # todo gallery, created_by

    class Meta:
        db_table = "odyssey"
        verbose_name = "Odyssey"
        verbose_name_plural = "Odyssies"

    def __str__(self):
        return f"{self.from_place} - {self.destination_place}"

class Requests(BaseModel):
    user = models.ForeignKey(User, verbose_name='User', related_name='requests', related_query_name='request', on_delete=models.CASCADE)
    odyssey = models.ForeignKey(Odyssey, verbose_name='Odyssey', related_name='odyssies', related_query_name='odyssey', on_delete=models.CharField)
    requested_date = models.DateField(verbose_name='Requested Date')
    is_accepted = models.BooleanField(verbose_name='Is accepted', blank=True, null=True)

    class Meta:
        db_table = "requests"
        verbose_name = "Request"
        verbose_name_plural = "Requests"
