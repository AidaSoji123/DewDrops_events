from django.db import models


class EventEnquiry(models.Model):
 
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=200)
    number_of_guests = models.PositiveIntegerField()
    services_needed = models.TextField()
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    additional_comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Enquiry from {self.contact_name} for {self.event_type}"


    class Meta:
        db_table = 'enquiry_tb'