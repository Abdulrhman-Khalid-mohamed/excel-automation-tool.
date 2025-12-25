import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def clean_data(file_path, output_file):
    try:
        df = pd.read_excel(file_path)
        df.drop_duplicates(inplace=True)
        df.fillna("N/A", inplace=True)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        df.to_excel(output_file, index=False)
        logging.info(f"Cleaned data saved to {output_file}")
    except Exception as e:
        logging.error(f"Error cleaning data: {e}")
