# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

## Closed Issues:

Issue 1-

The render_template function was incorrectly mocked to return a MagicMock object. This mock object was passed as the HTML content to the send_email method, leading to a failure in the assert_called_once_with assertion when verifying the method's arguments.


