import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

builder.insert_image("2.png")

doc.save("Output.docx")
