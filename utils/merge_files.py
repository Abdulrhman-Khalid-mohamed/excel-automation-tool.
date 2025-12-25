import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

def merge_excel_files(input_folder, output_file):
    try:
        all_files = [f for f in os.listdir(input_folder) if f.endswith(('.xlsx', '.csv'))]
        if not all_files:
            logging.warning("No Excel/CSV files found in folder.")
            return
        df_list = []
        for file in all_files:
            file_path = os.path.join(input_folder, file)
            df = pd.read_csv(file_path) if file.endswith('.csv') else pd.read_excel(file_path)
            df_list.append(df)
        merged_df = pd.concat(df_list, ignore_index=True)
        merged_df.to_excel(output_file, index=False)
        logging.info(f"Merged {len(all_files)} files into {output_file}")
    except Exception as e:
        logging.error(f"Error merging files: {e}")
