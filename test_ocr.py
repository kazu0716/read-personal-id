from PIL import Image
import sys
import pyocr
import pyocr.builders


def main():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))

    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))

    for i in range(1, 16):
        file_name = './images/fake_{}.png'.format(str(i))
        txt = tool.image_to_string(
            Image.open(file_name),
            lang="eng+jpn",
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )
        print("--{}--".format(file_name))
        print(txt)


if __name__ == '__main__':
    main()
