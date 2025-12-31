from crewai.tools import BaseTool
import pandas as pd


class CSVAnalysisTool(BaseTool):
    name: str = "csv_analysis_tool"
    description: str = (
        "Analyze a CSV file and return key insights such as trends, "
        "missing values, and statistical summary."
    )

    def _run(self, file_path: str) -> dict:
        df = pd.read_csv(file_path)

        insights = {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_values": df.isnull().sum().to_dict(),
            "summary_statistics": df.describe(include="all").to_dict()
        }

        return insights
