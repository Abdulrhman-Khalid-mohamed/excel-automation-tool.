import argparse
import os
import logging
from utils.merge_files import merge_excel_files
from utils.clean_data import clean_data
from utils.generate_report import generate_summary
import config

logging.basicConfig(level=logging.INFO)

def send_email(file_path):
    if not config.EMAIL_ENABLED:
        return
    import smtplib
    from email.message import EmailMessage
    try:
        msg = EmailMessage()
        msg["Subject"] = "Automation Report"
        msg["From"] = config.EMAIL_SENDER
        msg["To"] = config.EMAIL_RECEIVER
        msg.set_content("Please find the attached report.")
        with open(file_path, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="xlsx", filename=os.path.basename(file_path))
        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
            server.send_message(msg)
        logging.info(f"Report emailed to {config.EMAIL_RECEIVER}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def main():
    parser = argparse.ArgumentParser(description="Excel Automation Tool")
    parser.add_argument("--merge", action="store_true", help="Merge files")
    parser.add_argument("--clean", action="store_true", help="Clean merged file")
    parser.add_argument("--report", action="store_true", help="Generate summary report")
    args = parser.parse_args()

    merged_file = os.path.join(config.OUTPUT_FOLDER, "merged.xlsx")
    cleaned_file = os.path.join(config.OUTPUT_FOLDER, "cleaned.xlsx")
    report_file = os.path.join(config.OUTPUT_FOLDER, "summary.xlsx")

    if args.merge:
        merge_excel_files(config.SAMPLE_FOLDER, merged_file)
    if args.clean:
        clean_data(merged_file, cleaned_file)
    if args.report:
        generate_summary(cleaned_file, report_file)
        send_email(report_file)

    if not any([args.merge, args.clean, args.report]):
        logging.info("No arguments provided. Use --help for usage information.")

if __name__ == "__main__":
    main()
