import gradio as gr
import pandas as pd

def load_file():
    return gr.update(visible=True)

def show_outputs():
    return gr.update(visible=True), gr.update(visible=True), \
        gr.update(visible=True), gr.update(visible=True)

def hide_outputs():
    return gr.update(value=pd.DataFrame(), visible=False), gr.update(visible=False), \
        gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def parse_pdf(file):
    data = {
        'StringColumn': ['Row1', 'Row2', 'Row3', 'Row4', 'Row5'],
        'FloatColumn': [1.1, 2.2, 3.3, 4.4, 5.5]
    }
    df = pd.DataFrame(data)
    if file is not None:
        fn = file.name.split(".")[0]
    path_ext = lambda ext: f"{fn}_parsed.{ext}" 
    csv_path = path_ext("csv")
    xlsx_path = path_ext("xlsx")
    json_path = path_ext("json")
    
    df.to_csv(csv_path, index=False)
    df.to_excel(xlsx_path, index=False)
    df.to_json(json_path, index=False)
  
    return df, csv_path, xlsx_path, json_path

def create_interface(title: str = "gradio app"):
    interface = gr.Blocks(title=title)
    with interface:
        gr.Markdown("# Parsing IFRS financial statements from PDF using mistralAI LLM")
        pdf_input = gr.File(label="Upload PDF file", file_types=[".pdf",], height=160, )
        process_btn = gr.Button(value="Parse pdf data", visible=False, variant="primary")
        parsed_reports = gr.DataFrame(label="Parsed financial statements", 
                                        show_copy_button=True, 
                                        visible=False, min_width=10)
        with gr.Row():
            download_csv = gr.File(label="Download as CSV", visible=False)
            download_xlsx = gr.File(label="Download as XLSX", visible=False)
            download_json = gr.File(label="Download as JSON", visible=False)


        pdf_input.upload(load_file, None, process_btn)
        process_btn.click(parse_pdf, [pdf_input], 
                         [parsed_reports, download_csv, download_xlsx, download_json], queue=True)
        process_btn.click(show_outputs, None, [parsed_reports, download_csv, download_xlsx, download_json], queue=True)
        pdf_input.clear(hide_outputs, None, [parsed_reports, download_csv, download_xlsx, download_json, process_btn])

    return interface

if __name__ == "__main__":
    create_interface().launch()
        