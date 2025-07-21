import gradio as gr
import pandas as pd
try:    # for running interface.py
    import utils
    from config import mistral_params
    from logger import setup_logger
except: # for running main.py
    from . import utils
    from .config import mistral_params
    from .logger import setup_logger

logger = setup_logger()


def show_outputs():
    logger.info("Processing done")
    return gr.update(visible=True), gr.update(visible=True), \
        gr.update(visible=True), gr.update(visible=True)

def hide_outputs():
    logger.debug("File was closed")
    return gr.update(value=pd.DataFrame(), visible=False), gr.update(visible=False), \
        gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def parse_pdf(file):
    """
    This function extracts tables from a given PDF file, processes the text
    using a language model, and saves the results into CSV, Excel, and JSON
    formats.

    Args:
        file (file-like object): The PDF file to be parsed.

    Returns:
        tuple: A tuple containing:
            - pd.DataFrame: A DataFrame with the parsed indicators and values.
            - str: The name of CSV file.
            - str: The name of Excel file.
            - str: The name of JSON file.

    Raises:
        Exception: If an error occurs during the parsing process.
    """
    logger.info("Starting to parse PDF file: %s", file.name)
    
    try:
        tables_txt = utils.extract_tabels(file)
        logger.debug("Extracted tables text")

        llm = utils.create_model(mistral_params)
        logger.debug("Model created successfully.")

        parsed_dict = utils.process_txt(tables_txt, llm)
        logger.debug("Parsed dictionary: %s", parsed_dict)

        fn = file.name.split(".")[0]
        path_ext = lambda ext: f"{fn}_parsed.{ext}"
        csv_path = path_ext("csv")
        xlsx_path = path_ext("xlsx")
        json_path = path_ext("json")

        df = pd.DataFrame(list(parsed_dict.items()), columns=['Indicator', 'Value'])
        df.to_csv(csv_path, index=False)
        df.to_excel(xlsx_path, index=False)
        df.to_json(json_path, index=False)

    except Exception as e:
        logger.error("An error occurred while parsing the PDF: %s", e)
        raise e
    return df, csv_path, xlsx_path, json_path


def create_interface(title: str = "gradio app"):
    interface = gr.Blocks(title=title)
    with interface:
        gr.Markdown("# Parsing IFRS financial statements from PDF using LLM")
        pdf_input = gr.File(label="Upload PDF file", file_types=[".pdf",], height=160, )
        process_btn = gr.Button(value="Parse pdf data", visible=False, variant="primary")
        parsed_reports = gr.DataFrame(label="Parsed financial statements", 
                                        show_copy_button=True, 
                                        visible=False, min_width=10)
        with gr.Row():
            download_csv = gr.File(label="Download as CSV", visible=False)
            download_xlsx = gr.File(label="Download as XLSX", visible=False)
            download_json = gr.File(label="Download as JSON", visible=False)


        pdf_input.upload(lambda: gr.update(visible=True), None, process_btn)
        process_btn.click(parse_pdf, [pdf_input], 
                         [parsed_reports, download_csv, download_xlsx, download_json], queue=True)
        process_btn.click(show_outputs, None, [parsed_reports, download_csv, download_xlsx, download_json], queue=True)
        pdf_input.clear(hide_outputs, None, [parsed_reports, download_csv, download_xlsx, download_json, process_btn])

    return interface

if __name__ == "__main__":
    create_interface().launch()
        