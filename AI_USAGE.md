
# AI Tool Used

ChatGPT

# How AI Was Used

ChatGPT was used as a development assistant during the assignment.

It was used to:
- Help set up the Django project.
- Review the assignment requirements.
- Suggest the Django models.
- Help implement the box recommendation logic.
- Help create the Django endpoint.
- Help create automated test cases.
- Help prepare project documentation.

## Prompts Given

Examples of prompts used during development:

- "this is the task i need to do"
- "we need to do exact thing what they say in the doc no extra implementation"
- Questions and instructions related to implementing and testing the Django assignment.

## Output Accepted

The following AI-assisted code was reviewed and used:

- Product and Box Django models.
- Box recommendation service.
- Recommendation endpoint.
- URL configuration.
- Automated test cases.

## Output Rejected or Modified

The implementation was kept limited to the requirements of the assignment.

Any unnecessary features or additional functionality suggested during development were not included.

## Mistakes Found

The implementation was tested manually and with Django's automated test framework.

The test cases were used to verify:
- Suitable box selection.
- Weight capacity validation.
- Dimension validation.

## Verification

The application was verified by:

1. Running Django migrations successfully.
2. Adding products and boxes through Django Admin.
3. Calling the recommendation endpoint manually.
4. Confirming the expected JSON response.
5. Running:

```bash
python manage.py test