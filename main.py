import cv2
import numpy as np
import os
import sys


def add_black_background(input_image_path, output_image_path):
    # Load the input image
    input_image = cv2.imread(input_image_path)

    if input_image.shape[0] == input_image.shape[1]:
        return

    # Determine the new background size (it should be a square of the max dimension of the input image)
    max_dimension = max(input_image.shape[:2])
    background = np.zeros((max_dimension, max_dimension, 3), dtype=np.uint8)  # Black background

    # Calculate the center position
    x_center = (max_dimension - input_image.shape[1]) // 2
    y_center = (max_dimension - input_image.shape[0]) // 2

    # Place the input image onto the center of the black square background
    background[y_center:y_center + input_image.shape[0], x_center:x_center + input_image.shape[1]] = input_image

    # Save the combined image as JPEG
    cv2.imwrite(output_image_path, background, [int(cv2.IMWRITE_JPEG_QUALITY), 50])


def add_white_background(input_image_path, output_image_path):
    # Load the input image
    input_image = cv2.imread(input_image_path)

    # Determine the new background size (it should be a square of the max dimension of the input image)
    if input_image.shape[0] == input_image.shape[1]:
        return
    max_dimension = max(input_image.shape[:2])
    # Create a white background instead of black
    background = np.ones((max_dimension, max_dimension, 3), dtype=np.uint8) * 255

    # Calculate the center position
    x_center = (max_dimension - input_image.shape[1]) // 2
    y_center = (max_dimension - input_image.shape[0]) // 2

    # Place the input image onto the center of the white square background
    background[y_center:y_center + input_image.shape[0], x_center:x_center + input_image.shape[1]] = input_image

    # Save the combined image as JPEG
    cv2.imwrite(output_image_path, background, [int(cv2.IMWRITE_JPEG_QUALITY), 50])


def walk_through(dest_path: str, white=True):
    for root, dirs, files in os.walk(dest_path, topdown=False):
        for name in files:
            if white:
                add_white_background(os.path.join(root, name), os.path.join(root, f"wbg_{name}"))
            else:
                add_black_background(os.path.join(root, name), os.path.join(root, f"bbg_{name}"))


def main(dest_path, white):
    walk_through(dest_path, white)


if __name__ == '__main__':
    main(sys.argv[1], False)
