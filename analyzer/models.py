from django.db import models
class LogEntry(models.Model):
    timestamp=models.DateTimeField()
    action=models.CharField(max_length=16)
    protocol=models.CharField(max_length=8)
    src_ip=models.CharField(max_length=45)
    dst_ip=models.CharField(max_length=45)
    dst_port=models.IntegerField(null=True,blank=True)
    raw=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.timestamp} {self.action} {self.src_ip}->{self.dst_ip}:{self.dst_port}"
class Alert(models.Model):
    level=models.CharField(max_length=16)
    message=models.TextField()
    related_ip=models.CharField(max_length=45,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.level} - {self.message[:80]}"
