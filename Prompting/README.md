## Process
- Develop test cases for the prompting strategies.
- Use these to generate results for new test cases.

## Structure
- The test cases have been named as <TestCase-1 type.md> where type can be
  - FS: Few Shot
  - ZS: Zero Shot
- The folders contain the answers provided by every model

## Testing
- For Zero shot learning you can provide just the test cases to the LLM
- For Few shot learning you will need to provide the sample and the new test case in a single prompt.

## Results
- The results can be found in the [Results.md](Results.md) file.