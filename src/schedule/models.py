from django.db import models
from pytz import all_timezones

# --------------------------------
# Student Model
# --------------------------------
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    time_zone = models.CharField(
        max_length=50,
        default='UTC',
    )

    def __str__(self):
        return self.name


# --------------------------------
# Subject Model
# --------------------------------
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# --------------------------------
# Tutor Model
# --------------------------------
class Tutor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    time_zone = models.CharField(
        max_length=50,
        default='UTC',
    )
    subjects = models.ManyToManyField(Subject, related_name='tutors')

    def __str__(self):
        return f"{self.name} ({', '.join([s.name for s in self.subjects.all()])})"


# --------------------------------
# Availability Model
# --------------------------------
class Availability(models.Model):
    """
    Represents a block of time a tutor is available.
    """
    DAY_OF_WEEK_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]
    
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='availabilities')
    is_recurring = models.BooleanField(default=False)
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES, null=True, blank=True)
    date = models.DateField(null=True, blank=True)  # Only used for non-recurring availability
    start_time = models.TimeField()  # Local time stored as is
    end_time = models.TimeField()    # Local time stored as is

    def __str__(self):
        if self.is_recurring:
            return f"{self.tutor.name} - Recurring on {self.get_day_of_week_display()} {self.start_time} to {self.end_time} ({self.time_zone})"
        else:
            return f"{self.tutor.name} - One-time on {self.date} {self.start_time} to {self.end_time} ({self.time_zone})"


# --------------------------------
# Booking Model
# --------------------------------
class Booking(models.Model):
    """
    Stores information about a booked time slot between a Student and a Tutor
    for a particular Subject.
    """
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Booking for {self.student.name} with {self.tutor.name} "
            f"({self.subject.name if self.subject else 'No Subject'}) "
            f"from {self.start_time} to {self.end_time} - {self.status}"
        )