# import module
# from pdf2image import convert_from_path


# # Store Pdf with convert_from_path function
# images = convert_from_path('./fw9.pdf')

# for i in range(len(images)):

# 	# Save pages as images in the pdf
# 	images[i].save('page'+ str(i) +'.jpg', 'JPEG')

# from pdf2image import convert_from_path
# images = convert_from_path('fw9.pdf', 50)
# for image in images:
#     image.save('output.png')


from pdf2image import convert_from_path

title = input("Pdf files name: ")


def menu():
    global quality
    print("""
        Image format: 
        1. Very High Resolution - 700 dpi
        2. High Resolution - 500 dpi
        3. Medium Resolution - 300 dpi
        4. Low Resolution - 100 dpi
        5. Very Low Resolution - 50 dpi
        """)
    while True:
        choice = input('Choose One: ')
        quality = 700 if choice == '1' else 500 if choice == '2' else 300 if choice == '3' else 100 if choice == '4' else 50 if choice == '5' else "Wrong choice"
        program()
        print('Have a Nice Code')
        quit()


def program():
    images = convert_from_path(f'{title}.pdf', quality)
    for i, image in enumerate(images):
        image.save(f'./img/save_{i}.png')


if __name__ == '__main__':
    menu()