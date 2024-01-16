import logging

import cv2
import numpy as np

from mvp_sneakers_api.settings.settings import settings

logger = logging.getLogger()


# pylint: disable=no-member
def infer_model(model, image: bytes):
    """
    Perform inference using a pre-trained model on an input image.

    Parameters:
    - model: The pre-trained machine learning model
    (e.g., scikit-learn model) loaded using pickle.
    - image: Bytes representation of the input image.

    Returns:
    - dict: A dictionary containing the predicted label.
    """
    np_array = np.frombuffer(image, np.uint8)

    decoded_img = cv2.imdecode(np_array, cv2.IMREAD_GRAYSCALE)
    decoded_img = cv2.resize(
        decoded_img, (settings.model.image_size, settings.model.image_size)
    )

    img_flat = np.asarray(decoded_img).flatten()
    prediction = model.predict(np.expand_dims(img_flat, axis=0))[0]

    if prediction in settings.model.label:
        predicted_label = settings.model.label[prediction]
    else:
        predicted_label = "Unknown"

    return {"Label": predicted_label}
