
def upload_pizza_image(instance, filename):
    return f"pizza-image-{str(instance).replace("-> ", "")}-{filename}"


def upload_producer_logo_image(instance, filename):
    return f"producer-logo-{instance}-{filename}"
