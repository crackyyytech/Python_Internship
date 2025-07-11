import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

def load_csv_data(file_path):
    return pd.read_csv(file_path)

def generate_summary_stats(df):
    return df.describe()

def generate_bar_plot(df, column, output_file="bar_plot.png"):
    plt.figure(figsize=(6, 4))
    df[column].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f"{column} Distribution")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

def create_pdf_report(summary, plot_path, output_pdf="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Automated Data Report", ln=True, align='C')
    pdf.ln(10)

    for column in summary.columns:
        pdf.cell(200, 10, txt=f"Summary for {column}", ln=True)
        for stat in summary.index:
            value = summary.loc[stat, column]
            pdf.cell(200, 10, txt=f"{stat}: {value:.2f}", ln=True)
        pdf.ln(5)

    pdf.image(plot_path, x=10, y=None, w=180)
    pdf.output(output_pdf)

if __name__ == "__main__":
    csv_file = "students.csv"
    df = load_csv_data(csv_file)
    summary = generate_summary_stats(df)
    generate_bar_plot(df, "Grade")
    create_pdf_report(summary, "bar_plot.png")
