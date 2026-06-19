report = """
Daily Job Report

Project Officer
Score: 88

Project Coordinator
Score: 82
"""

with open("job_report.txt", "w") as file:
    file.write(report)

print("Report Created")
