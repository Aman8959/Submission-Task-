import pandas as pd
import numpy as np

np.random.seed(42)

# Table 1: Students registered in the system
students = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105, 106],
    "name":       ["Arjun", "Priya", "Sneha", "Dev", "Meera", "Kiran"],
    "city":       ["Mumbai", "Delhi", "Bangalore", "Pune", "Mumbai", "Chennai"]
})

# Table 2: Exam scores (not every student appeared)
scores = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 107],
    "math":       [88,  76,  91,  65,  70],
    "science":    [72,  84,  88,  55,  80],
    "english":    [90,  68,  95,  72,  85]
})

# Table 3: Attendance records (some students have no record)
attendance = pd.DataFrame({
    "student_id":       [101, 103, 104, 105],
    "attendance_pct":   [92.0, 88.5, 71.0, 95.5]
})

# Part 1 — Understand the Data
print("Students shape:", students.shape)
print(students.head(), end="\n\n")

print("Scores shape:", scores.shape)
print(scores.head(), end="\n\n")

print("Attendance shape:", attendance.shape)
print(attendance.head(), end="\n\n")

# Count students with no scores and no attendance record
student_scores_left = students.merge(scores, on="student_id", how="left")
no_scores_count = student_scores_left[student_scores_left[["math", "science", "english"]].isna().all(axis=1)].shape[0]
no_attendance_count = students.merge(attendance, on="student_id", how="left")["attendance_pct"].isna().sum()

print("Students registered but with NO scores:", no_scores_count)
print("Students registered but with NO attendance record:", no_attendance_count, end="\n\n")

# Part 2 — Build the Report Card
student_scores = students.merge(scores, on="student_id", how="left")
report_card = student_scores.merge(attendance, on="student_id", how="left")

print("Report card after merges:")
print(report_card, end="\n\n")

print("Students with NaN values in report_card:")
print(report_card[report_card.isna().any(axis=1)], end="\n\n")
print("Explanation: NaN values appear for students who did not appear in the exam or who have no attendance record.")
print("- Missing scores: student registered but absent from the scores table.")
print("- Missing attendance: student registered but absent from the attendance table.", end="\n\n")

# Part 3 — Enrich and Clean
report_card["avg_score"] = report_card[["math", "science", "english"]].mean(axis=1)

conditions = [
    report_card["avg_score"] >= 85,
    report_card["avg_score"] >= 70,
    report_card["avg_score"] >= 55
]
choices = ["A", "B", "C"]
report_card["grade"] = np.select(conditions, choices, default="F")
report_card.loc[report_card[["math", "science", "english"]].isna().all(axis=1), "grade"] = "F"

print("Final report_card with avg_score and grade:")
print(report_card, end="\n\n")

# Top performers summary
top_performers = report_card[report_card["grade"] == "A"]
print("Top performers (grade A):")
print(top_performers, end="\n\n")

# Part 4 — Multi-Source Insight
never_appeared = students[~students["student_id"].isin(scores["student_id"])]
print("Students registered but never appeared for the exam:", never_appeared["name"].tolist())
print("Count:", never_appeared.shape[0], end="\n\n")

# Save final report_card
report_card.to_csv("report_card.csv", index=False)
print("Saved final report card to report_card.csv")
