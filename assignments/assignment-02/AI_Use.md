# AI Assistance Record

## Tools Used
- Gemini (Google AI)

## Prompts and Responses
1. **Prompt**: "How to replace values outside 0-120 with NaN in a pandas column?"
   - **Response**: Suggested using boolean filtering with `.loc` and `np.nan`.
2. **Prompt**: "How to format a clean README markdown table for test predictions?"
   - **Response**: Provided standard markdown syntax for creating comparison tables.

## Improvements Made to AI Suggestions
- The initial AI example replaced missing values immediately with mean. I rejected that and wrote the logic myself using median from valid records only, as required by the assignment rules.

## Testing Evidence
- Ran `uv run python Assignment_02/test_patient_dataset.py` in the terminal and verified that all assertion checks passed.