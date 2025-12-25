import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def generate_summary(file_path, output_file):
    try:
        df = pd.read_excel(file_path)
        summary = df.describe(include='all')
        summary.to_excel(output_file)
        logging.info(f"Summary report saved to {output_file}")
    except Exception as e:
        logging.error(f"Error generating report: {e}")
