import re

# Sample input text
text = """
Emails:
rajveer@example.com, first.last@company.co.uk

URLs:
https://www.example.com, https://sub.example.org/page

Phone Numbers:
(123) 456-7890, 123-456-7890, 123.456.7890

Credit Cards:
1234 5678 9012 3456, 1234-5678-9012-3456

Time:
14:30, 2:30 PM

HTML Tags:
<p>, <div class="example">, <img src="image.jpg" alt="description">

Hashtags:
#example, #ThisIsAHashtag

Currency:
$19.99, $1,234.56
"""

# REGEX PATTERNS
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_pattern = r'https?://[^\s<>"]+'
phone_pattern = r'(\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}'
hashtag_pattern = r'#\w+'

# FIND ALL
emails = re.findall(email_pattern, text)
urls = re.findall(url_pattern, text)
phones = re.findall(phone_pattern, text)
hashtags = re.findall(hashtag_pattern, text)

# DISPLAY RESULTS
print("📧 Emails:", emails)
print("🔗 URLs:", urls)
print("📞 Phones:", phones)
print("🏷️ Hashtags:", hashtags)
