from PIL import Image, ImageOps
import imagehash


def ahash(file1, file2):
    fake_hash1 = imagehash.average_hash(
        ImageOps.grayscale(ImageOps.grayscale(Image.open(file1))))
    fake_hash2 = imagehash.average_hash(
        ImageOps.grayscale(ImageOps.grayscale(Image.open(file2))))
    print("fake_hash1", fake_hash1)
    print("fake_hash2", fake_hash2)
    print("ahash diff text", fake_hash1-fake_hash2)


def dhash(file1, file2):
    fake_hash1 = imagehash.dhash(ImageOps.grayscale(Image.open(file1)))
    fake_hash2 = imagehash.dhash(ImageOps.grayscale(Image.open(file2)))
    print("fake_hash1", fake_hash1)
    print("fake_hash2", fake_hash2)
    print("dhash diff text", fake_hash1-fake_hash2)


def phash(file1, file2):
    fake_hash1 = imagehash.phash(ImageOps.grayscale(Image.open(file1)))
    fake_hash2 = imagehash.phash(ImageOps.grayscale(Image.open(file2)))
    print("fake_hash1", fake_hash1)
    print("fake_hash2", fake_hash2)
    print("phash diff text", fake_hash1-fake_hash2)


def main():
    for i in (1, 3, 5, 9, 11, 13, 15):
        print("=====")
        id_file1 = "./images/fake_{}.png".format(str(i))
        id_file2 = "./images/fake_{}.png".format(str(i+1))
        print("check defference of id-image from {} to {}".format(id_file1, id_file2))
        phash(id_file1, id_file2)
        print("---")

        cut_file1 = "./cut_faces/fake_{}.png".format(str(i))
        cut_file2 = "./cut_faces/fake_{}.png".format(str(i+1))
        print("check defference of face-image from {} to {}".format(cut_file1, cut_file2))
        ahash(cut_file1, cut_file2)
        print("---")

        text_file1 = "./hide_faces/fake_{}.png".format(str(i))
        text_file2 = "./hide_faces/fake_{}.png".format(str(i+1))
        print("check defference of text-image from {} to {}".format(text_file1, text_file2))
        dhash(text_file1, text_file2)
        print("=====")
        print("")

        # print("differ {} and {}".format(file1, file2))
        # print("------")
        # ahash(file1, file2)
        # print("---")
        # dhash(file1, file2)
        # print("---")
        # phash(file1, file2)
        # print("---")

    print("=====")
    id_file1 = "./images/fake_{}.png".format(str(7))
    id_file2 = "./images/fake_{}.png".format(str(7+1))
    print("check defference of id-image from {} to {}".format(id_file1, id_file2))
    dhash(id_file1, id_file2)
    print("---")


if __name__ == '__main__':
    main()
