# Student Support Rule Engine (Assignment 1)

## Program Description
A simple Python command-line tool that checks student attendance, average marks, and missed tasks to give academic advice.

## Support Priority Rules
1. **High priority**: Checked first. Triggers if attendance < 60% OR missed tasks >= 4.

2. **Moderate priority**: Checked second. Triggers if attendance < 75%, marks < 60%, OR missed tasks >= 2.

3. **Routine monitoring**: Assigned if all above checks are safe.

## Submitted Files
* `support_engine.py`: Program with input checks, logic rules, and advice.
* `test_support_engine.py`: Automated tests using assert statements.
* `README.md`: Short project notes, rules, commands, and limitations.

## Run and Test Commands
Run from the main folder (`Programming-for-AI-2026`):

Run the app:
```bash
uv run python assignments/assignment-01/support_engine.py

## Known Limitations
1. **Fixed Rules & Inputs**: Rule thresholds are hard-coded in the script, and it only checks three indicators while ignoring exams or GPA.
2. **No Storage & CLI Only**: Evaluated student records are not saved permanently, and the application runs solely in the terminal without a GUI.