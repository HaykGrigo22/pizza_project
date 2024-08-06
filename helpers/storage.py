
def upload_pizza_image(instance, filename):
    return f"pizza-image-{instance.title}-{filename}"


def upload_producer_logo_image(instance, filename):
    return f"producer-logo-{instance.producer_name}-{filename}"
