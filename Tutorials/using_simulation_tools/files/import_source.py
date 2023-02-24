import os
import requests


def cd(folder):
    """My wrapper for os.chdir() so I can print it desired."""
    if folder:
        os.chdir(folder)


def import_text(text):
    url = "https://raw.githubusercontent.com/westonMS/tempColab/main/Labs/bin/%s" % text
    resp = requests.get(url)
    with open(text, "wb") as f:
        f.write(resp.content)


def import_dataflow():
    cd("/content/tmp_code")
    import_text("TBtemplate.txt")
    import_text("simTemplate.txt")
    import_text("simTemplate2.txt")
    import_text("function1.sv")
    import_text("function1.stm")
    cd("/content")
