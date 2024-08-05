import sys

from PyPDF2 import PdfReader, PdfWriter


def reorder(path):
    pdf_writer = PdfWriter()
    try:
        pdf_reader = PdfReader(path)
    except(ValueError):
        print("No such file or directory")
        sys.exit()
    print("\nFile found")
    num_of_page = len(pdf_reader.pages)
    last_page_blank = input("Is the last page blank? [y/n]")
    print(f"Number of pages: {num_of_page}")
    page_list = [i + 1 for i in range(num_of_page)]
    final_list = []
    index = 1
    if num_of_page % 2 == 0:
        for i in range(num_of_page//2):
            operating_page = page_list[-1]
            final_list.append(index)
            final_list.append(operating_page)
            page_list.remove(page_list[-1])
            index += 1
    else:
        for i in range(num_of_page//2):
            operating_page = page_list[-1]
            final_list.append(index)
            final_list.append(operating_page)
            page_list.remove(page_list[-1])
            index += 1
        final_list.append(index)
    if last_page_blank == "y":
        final_list.remove(final_list[-1])

    print("\nFinal page order looks like this:")
    print(final_list)

    proceed = input("proceed?[y/n] ")
    if proceed == "y":
        for page in final_list:
            pdf_writer.add_page(pdf_reader.pages[page - 1])
        output_file = input("\nEnter file name: ") + '.pdf'
        with open("/Users/edwardqiu/Desktop/" + output_file, 'wb') as fh:
            pdf_writer.write(fh)
            print("\nFile export successful")
            print(f"Go to {output_file}")
    else:
        print("program terminated")
        sys.exit()


if __name__ == '__main__':
    path = input("Enter file path or drag file here: ")
    reorder(path)
