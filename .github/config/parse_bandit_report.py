from bs4 import BeautifulSoup

# Path to the Bandit HTML report
report_path = 'results.html'

# Read the HTML report
with open(report_path, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract summary and details
summary = {
    'HIGH': {'file_count': 0, 'issue_count': 0},
    'MEDIUM': {'file_count': 0, 'issue_count': 0},
    'LOW': {'file_count': 0, 'issue_count': 0}
}
details = []

# Parse the HTML to extract the relevant information
# (This part will depend on the structure of the Bandit HTML report)

# Example output (replace with actual parsing logic)
summary['MEDIUM']['file_count'] = 12
summary['MEDIUM']['issue_count'] = 17
summary['LOW']['file_count'] = 27
summary['LOW']['issue_count'] = 36

details.append({
    'file': 'example.py',
    'line_numbers': '10-20',
    'test': 'B101',
    'issue': 'Use of assert detected',
    'severity': 'MEDIUM',
    'confidence': 'HIGH'
})

# Print the summary and details
print("Summary of Issues")
print("Severity\tFile Count\tIssue Count")
for severity, counts in summary.items():
    print(f"{severity}\t{counts['file_count']}\t{counts['issue_count']}")

print("\nDetails of Issues")
print("File (Line Numbers)\tTest\tIssue\tSeverity\tConfidence")
for detail in details:
    print(f"{detail['file']} ({detail['line_numbers']})\t{detail['test']}\t{detail['issue']}\t{detail['severity']}\t{detail['confidence']}")
