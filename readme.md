# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

## Closed Issues:

Issue 1-

The render_template function was incorrectly mocked to return a MagicMock object. This mock object was passed as the HTML content to the send_email method, leading to a failure in the assert_called_once_with assertion when verifying the method's arguments.
Resolution: Updated the mock for render_template to return a realistic HTML string. This ensures the send_email function receives content in the correct format, and the assertion now passes as expected.

Issue 2-

The nickname generation feature is currently not working as intended. The generated nicknames are often invalid, lack uniqueness, or do not comply with the defined requirements.
Resolution: Fixed the code.

Issue 3-

Currently, we use UUIDs for authentication. To improve both user-friendliness and security, we suggest replacing the UUID-based system with email verification, as every user has a unique email address.
Resolution: Enhanced security through email validation.

Issue 4-

Develop a strong password validation logic to enhance security by enforcing requirements such as the combination of special characters, at least one uppercase letter, one lowercase letter, and at least one numeric digit.
Resolution: enforcing strong password requirements like special characters, at least one uppercase & lowercase and at least one numeric value.
