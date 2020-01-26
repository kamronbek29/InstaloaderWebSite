from django.db import models


class DownloadField(models.Model):
    download_field = models.URLField(unique=True, default=None)
