import cv2
import numpy as np


def main():
    for i in range(1, 17):
        read_file = "./images/fake_{}.png".format(str(i))

        # NOTE: some face train-data
        # face_pathes = (
        #     "haarcascade_frontalface_default.xml",
        #     # "haarcascade_frontalface_alt.xml",
        #     # "haarcascade_frontalface_alt2.xml",
        #     # "haarcascade_frontalface_alt_tree.xml",
        #     # "haarcascade_frontalcatface.xml",
        #     # "haarcascade_frontalcatface_extended.xml",
        #     # "haarcascade_profileface.xml",
        # )

        img_file = cv2.imread(read_file)
        gray_image = cv2.cvtColor(img_file, cv2.COLOR_RGB2GRAY)

        # for face_path in face_pathes:
        face_path = "haarcascade_frontalface_default.xml"
        face_cascade = cv2.CascadeClassifier(
            "/usr/local/share/OpenCV/haarcascades/{}".format(face_path)
        )
        facerect = face_cascade.detectMultiScale(
            gray_image,
            scaleFactor=1.11,
            minNeighbors=8,
            minSize=(50, 50),
            maxSize=(200, 200)
        )

        # NOTE: detect eyes
        # eye_path = "haarcascade_eye.xml"
        # eye_path = "haarcascade_eye_tree_eyeglasses.xml"
        # eye_cascade = cv2.CascadeClassifier(
        #     "/usr/local/share/OpenCV/haarcascades/{}".format(eye_path)
        # )
        # eyerect = eye_cascade.detectMultiScale(
        #     gray_image,
        #     scaleFactor=1.11,
        #     minNeighbors=2,
        #     minSize=(3, 3),
        #     maxSize=(50, 50)
        # )
        if len(facerect) > 0:
            for f_rect in facerect:
                cut_image = gray_image[
                    f_rect[1]:f_rect[1]+f_rect[3],
                    f_rect[0]:f_rect[0]+f_rect[2]
                ]
            cut_file = "./cut_faces/fake_{}.png".format(str(i))
            cv2.imwrite(cut_file, cut_image)
            for f_rect in facerect:
                hide_image = cv2.rectangle(
                    gray_image,
                    tuple(f_rect[0:2]),
                    tuple(f_rect[0:2]+f_rect[2:4]),
                    (255, 255, 255),  # NOTE: color white
                    thickness=-1
                )
            hide_file = "./hide_faces/fake_{}.png".format(str(i))
            cv2.imwrite(hide_file, hide_image)

        # NOTE: write eyes_rect
        # if len(facerect) > 0:
        # dst_image=cv2.rectangle(dst_image,
        #                           tuple(f_rect[0:2]),
        #                           tuple(f_rect[0:2]+f_rect[2:4]),
        #                           color,
        #                           thickness=2
        #                           )
        # print("tuple", tuple(f_rect[0:2]),
        #       tuple(f_rect[0:2]+f_rect[2:4])
        #       )

        # for e_rect in eyerect:
        #     dst_image=cv2.rectangle(dst_image,
        #                               tuple(e_rect[0:2]),
        #                               tuple(e_rect[0:2]+e_rect[2:4]),
        #                               color,
        #                               thickness=2
        #                               )


if __name__ == '__main__':
    main()
