import fitz  # PyMuPDF

def remove_text_from_pdf(input_pdf_path, output_pdf_path):
    """ PDF에서 텍스트를 제거하는 함수 """
    doc = fitz.open(input_pdf_path)

    for page in doc:
        text_instances = page.get_text("dict")["blocks"]
        for block in text_instances:
            if block['type'] == 0:  # 텍스트 블록만 처리
                bbox = block['bbox']
                page.draw_rect(bbox, color=(1, 1, 1), fill=True)  # 흰색으로 덮기

    doc.save(output_pdf_path)
    doc.close()
