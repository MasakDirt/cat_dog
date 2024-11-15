import tensorflow as tf


IMAGE_SIZE = (180, 180)


def process_image(image):
    img_array = tf.keras.utils.img_to_array(image)
    img_array = tf.keras.ops.expand_dims(img_array, 0)

    return img_array


def load_and_process_image(path: str) -> str:
    img = tf.keras.utils.load_img(path, target_size=IMAGE_SIZE)

    return process_image(img)


def classify(model, image_path: str) -> tuple[str, float]:
    image_array = load_and_process_image(image_path)

    predictions = model.predict(image_array)
    score = float(tf.keras.ops.sigmoid(predictions[0][0]))

    if score > 0.5:
        return "Dog", round(100 * score, 2)
    else:
        return "Cat", round(100 * (1 - score), 2)
