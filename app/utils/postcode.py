import re

POSTCODE_REGEX = r"^[A-Z]{1,2}[0-9R][0-9A-Z]?\ ?[0-9][ABD-HJLNP-UW-Z]{2}$"

def valid_postcode(postcode: str) -> bool:
  return bool(re.match(POSTCODE_REGEX, postcode))

def format_valid_postcode(postcode: str) -> str:
  trimmed = postcode.strip()

  formatted_postcode = " ".join(postcode.split()) if " " in trimmed else trimmed[:-3] + " " + trimmed[-3:]
  return formatted_postcode
  