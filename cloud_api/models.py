from django.db import models
from django.contrib.auth.models import User
import uuid

def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "{}.{}".format(uuid.uuid4().hex, ext)
    return 'user_{0}/{1}'.format(instance.user_id.id, filename)

class File_tb(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file_file = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    file_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    size_file = models.CharField(max_length =50, blank=True)
    create_at = models.DateTimeField(auto_created=True)
    last_download_time = models.DateTimeField(null=True)
    file_type = models.CharField(max_length=20, blank=True, null=True)
    id_uuid = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return f"{self.file_name}, {self.description}"