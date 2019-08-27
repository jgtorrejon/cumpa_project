def upload_location(instance, filename):
    """
    Method for generated the path for save the media
    """
    Model = instance.__class__
    last_object = Model.objects.order_by("id").last()
    new_id = last_object.id + 1 if last_object else 1
    return "%s/%s/%s" % (Model.__name__, new_id, filename)
