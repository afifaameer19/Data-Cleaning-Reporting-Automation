import matplotlib.pyplot as plt

class ReportGenerator:

    def __init__(self, df):
        self.df = df

    def generate_summary(self):

        summary = self.df.describe(include="all")

        summary.to_excel("reports/summary_report.xlsx")

    def sales_chart(self):

        if 'Sales' in self.df.columns and 'Region' in self.df.columns:

            self.df.groupby('Region')['Sales'].sum().plot(kind='bar')

            plt.title("Sales by Region")
            plt.tight_layout()

            plt.savefig("reports/sales_chart.png")

            plt.close()