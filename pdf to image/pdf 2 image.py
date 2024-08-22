from pdf2image import convert_from_path 

old_pdf = convert_from_path("new.pdf",poppler_path="D:\4th sem\python\project\pdf to image\Release-24.02.0-0\poppler-24.02.0\Library\bin")

for i in range(len(old_pdf)):
    old_pdf[i].save("sunset.jpg","JPEG")

