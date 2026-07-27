from data_cleaning import DataCleaner
from report_generator import ReportGenerator

cleaner = DataCleaner("data/raw_data.csv")

df = cleaner.clean_data()

cleaner.save("data/cleaned_data.csv")

report = ReportGenerator(df)

report.generate_summary()

report.sales_chart()

print("Automation Completed Successfully")