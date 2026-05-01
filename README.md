# Report Card Data Merge

This workspace contains `data_merge.py`, a small pandas script that builds a student report card by merging student registration, exam scores, and attendance data.

## What the script does

1. Loads three DataFrames:
   - `students`
   - `scores`
   - `attendance`
2. Prints the shape and first few rows of all three DataFrames.
3. Identifies:
   - how many students are registered but have no scores
   - how many registered students have no attendance record
4. Builds `student_scores` using a left join between `students` and `scores` on `student_id`.
5. Builds `report_card` using a left join between `student_scores` and `attendance` on `student_id`.
6. Prints `report_card` and highlights rows with `NaN` values.
7. Adds `avg_score` as the mean of `math`, `science`, and `english`.
8. Adds a `grade` column using the following logic:
   - `A` if `avg_score >= 85`
   - `B` if `avg_score >= 70`
   - `C` if `avg_score >= 55`
   - `F` if `avg_score < 55` or `avg_score` is `NaN`
9. Prints a "top performers" summary for students with grade `A`.
10. Prints students registered but never appeared for the exam.
11. Saves the final `report_card` DataFrame to `report_card.csv` without the index.

## Files

- `data_merge.py` - main script
- `report_card.csv` - generated output after running the script

## Run

```powershell
python data_merge.py
```

## Notes

- The script uses left joins to preserve all registered students.
- Missing scores or attendance values are represented as `NaN`.
- Student records with missing exam scores are still included in the final report card with grade `F`.
