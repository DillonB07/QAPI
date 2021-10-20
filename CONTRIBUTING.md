# Contributing to QAPI

If you want to contribute a question there are three ways!

1. Contribute via a Dizzle form
2. Contribute via a GitHub Issue
3. Contribute via a Pull Request

## Dizzle Form

Go to Dizzle's suggestion page and fill in the form. If you get an error, try again. If you still get an error, try the next method.

[Click to make a suggestion](https://dizzle.ml/suggest)

## QAPI Issue

Create an issue following the template to contribute!

[Click to create an issue](https://github.com/DillonB07/QAPI/issues/new?assignees=DillonB07&labels=question+suggestion&template=question_suggestion.md&title=%5BQ+Suggestion%5D+-+Question)

## Pull Request

Add a question in `questions.py` like so:

```python
question_number: {
    'type': 'memory', # Replace with the type of question
    'topic': 'literature', # Replace with the topic for the question
    'question': 'What has 2 legs?', # Replace with your question
    'option1': 'First option', # For multiple choice only
    'option2': 'Second option', # For multiple choice only
    'option3': 'Final option', # For multiple choice only
    'answer': 'Human' # Answer the question
}
```

Then create a Pull Request!
