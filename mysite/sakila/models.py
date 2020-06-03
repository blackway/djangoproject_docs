# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime
from django.db import models
from django.urls import reverse


class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)  # This field type is a guess.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'actor'


class AggregationAuthor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aggregation_author'


class AggregationBook(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    rating = models.FloatField()
    pubdate = models.DateField()
    publisher = models.ForeignKey('AggregationPublisher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'aggregation_book'


class AggregationBookAuthors(models.Model):
    book = models.ForeignKey(AggregationBook, models.DO_NOTHING)
    author = models.ForeignKey(AggregationAuthor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'aggregation_book_authors'
        unique_together = (('book', 'author'),)


class AggregationPublisher(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'aggregation_publisher'


class AggregationStore(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'aggregation_store'


class AggregationStoreBooks(models.Model):
    store = models.ForeignKey(AggregationStore, models.DO_NOTHING)
    book = models.ForeignKey(AggregationBook, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'aggregation_store_books'
        unique_together = (('store', 'book'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Category(models.Model):
    category_id = models.SmallIntegerField(primary_key=True)
    # category_id = models.AutoField()
    name = models.CharField(max_length=100)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'category'


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=100)
    last_update = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.country


class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='country_id')
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'city'
    def __str__(self):
        return self.country



class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    # id = models.IntegerField(primary_key=True, db_column='address_id')
    # address_id = models.AutoField()
    address = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500, blank=True, null=True)
    district = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, db_column='city_id')
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'address'

    def __str__(self):
        return self.address


class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    manager_staff_id = models.SmallIntegerField()
    # staff = models.ManyToManyField(Staff, through='Staff', db_column='manager_staff_id')
    # staff = models.ForeignKey(Staff, on_delete=models.CASCADE, db_column='manager_staff_id')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='address_id')
    # address_id = models.IntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'store'

    def __str__(self):
        return self.address.address


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='address_id')
    picture = models.BinaryField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='store_id')
    active = models.SmallIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'staff'


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(Store, blank=True, null=True, on_delete=models.SET_NULL, db_column='store_id')
    # store_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    active = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=datetime.now())  # This field type is a guess.
    last_update = models.DateTimeField(default=datetime.now())  # This field type is a guess. '%m/%d/%Y %H:%M:%S'

    class Meta:
        managed = False
        db_table = 'customer'

    def get_absolute_url(self):
        return reverse('sakila:customer_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Film(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    release_year = models.CharField(max_length=10, blank=True, null=True)
    language_id = models.SmallIntegerField()
    original_language_id = models.SmallIntegerField(blank=True, null=True)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    rating = models.CharField(max_length=10, blank=True, null=True)
    special_features = models.CharField(max_length=100, blank=True, null=True)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film'


class Film2019090401(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    release_year = models.CharField(max_length=100, blank=True, null=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    original_language_id = models.SmallIntegerField(blank=True, null=True)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    rating = models.CharField(max_length=10, blank=True, null=True)
    special_features = models.CharField(max_length=100, blank=True, null=True)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film_20190904-01'


class FilmActor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    film_id = models.IntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film_actor'


class FilmCategory(models.Model):
    film_id = models.IntegerField(primary_key=True)
    category_id = models.SmallIntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film_category'


class FilmText(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'film_text'


class Inventory(models.Model):
    inventory_id = models.IntegerField(primary_key=True)
    film_id = models.IntegerField()
    store_id = models.IntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'inventory'


class Language(models.Model):
    language_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'language'


class Language2019090401(models.Model):
    language_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'language-20190904-01'


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    staff_id = models.SmallIntegerField()
    rental_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    payment_date = models.TextField()  # This field type is a guess.
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'payment'


class PollsChoice(models.Model):
    choice_id = models.IntegerField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Rental(models.Model):
    rental_id = models.IntegerField(primary_key=True)
    rental_date = models.TextField()  # This field type is a guess.
    inventory_id = models.IntegerField()
    customer_id = models.IntegerField()
    return_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    staff_id = models.SmallIntegerField()
    last_update = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory_id', 'customer_id'),)


