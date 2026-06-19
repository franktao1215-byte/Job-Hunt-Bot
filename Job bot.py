job_description = """
This role involves project coordination,
stakeholder engagement,
report writing
and partnership development.
"""

score = 0

if "project" in job_description.lower():
    score += 20

if "stakeholder" in job_description.lower():
    score += 15

if "partnership" in job_description.lower():
    score += 15

if "report" in job_description.lower():
    score += 10

print("Match Score:", score)
