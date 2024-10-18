import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file_path, start_page, end_page, pages_per_file):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' was not found.")
        return

    # Load the PDF
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)

    # Adjust start and end pages based on user input
    start_page = start_page - 1 if start_page > 0 else 0
    end_page = end_page if end_page > 0 else total_pages

    # Validate the page range
    if start_page >= total_pages or end_page > total_pages or start_page >= end_page:
        print("Error: The page range is invalid.")
        return

    # Generate output files in parts based on the specified page count
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = "pdf_parts"
    os.makedirs(output_dir, exist_ok=True)
    
    part_number = 1
    current_page = start_page
    
    while current_page < end_page:
        # Define the page range for each part
        block_end_page = min(current_page + pages_per_file, end_page)
        writer = PdfWriter()
        
        for page in range(current_page, block_end_page):
            writer.add_page(reader.pages[page])
        
        output_path = os.path.join(output_dir, f"{base_name}_part{part_number}.pdf")
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        
        print(f"Created: {output_path}")
        
        # Update variables for the next iteration
        current_page = block_end_page
        part_number += 1

    print(f"Task completed! The files have been saved in the '{output_dir}' folder.")

# Collect user inputs
file_path = input("Enter the PDF file path: ")
start_page = input("Enter the start page (or press Enter to start from the first page): ")
end_page = input("Enter the end page (or press Enter to go to the last page): ")
pages_per_file = input("Enter the number of pages per block (or press Enter to use blocks of 10 pages): ")

# Convert inputs to integers, using default values when appropriate
start_page = int(start_page) if start_page.strip() else 1
end_page = int(end_page) if end_page.strip() else 0
pages_per_file = int(pages_per_file) if pages_per_file.strip() else 10

# Execute the PDF splitting function
split_pdf(file_path, start_page, end_page, pages_per_file)
