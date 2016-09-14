def image_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/<object_title>/<filename>
    return '{0}/{1}'.format(instance.title, filename)

