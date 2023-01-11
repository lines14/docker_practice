import docx

def gettext(filename):
    doc = docx.Document(filename)
    Text = []
    for para in doc.paragraphs:
        Text.append(para.text)
    return '\n'.join(Text)