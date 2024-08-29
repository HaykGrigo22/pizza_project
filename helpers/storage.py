
def upload_pizza_image(instance, filename):
    return f"pizza-image-{instance.title}-{filename}"


def upload_burger_image(instance, filename):
    return f"burger-image-{instance.title}-{filename}"


def upload_producer_logo_image(instance, filename):
    return f"producer-logo-{instance.producer_name}-{filename}"


def upload_user_image(instance, filename):
    return f"user-image-{instance.title}-{filename}"
