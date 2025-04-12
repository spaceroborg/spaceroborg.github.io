import json
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: A list of dictionaries containing page numbers and text.
    """
    reader = PdfReader(pdf_path)
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages.append({"page": i + 1, "text": text.strip()})
    return pages

def save_markdown(pages, output_path):
    """
    Saves the extracted text to a Markdown file.

    Args:
        pages (list): A list of dictionaries containing page numbers and text.
        output_path (str): Path to save the Markdown file.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        for page in pages:
            f.write(f"# Page {page['page']}\n\n")
            f.write(page["text"])
            f.write("\n\n---\n\n")  # Add a separator between pages

def main():
    # Print current path
    import os
    print("Current working directory:", os.getcwd())

    pdf_path = "docs/files/SGBA_author_draft_full.pdf"  # Replace with your PDF file path
    output_path = "output.md"  # Replace with your desired Markdown file path

    print("Extracting text from PDF...")
    pages = extract_text_from_pdf(pdf_path)

    print(f"Saving extracted text to {output_path}...")
    save_markdown(pages, output_path)

    print("Done!")

if __name__ == "__main__":
    main()