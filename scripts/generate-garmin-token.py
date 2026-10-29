# /// script
# requires-python = ">=3.12"
# dependencies = ["garminconnect>=0.3.3"]
# ///
import getpass
import pathlib
import warnings

from garminconnect import Garmin

email = input("Garmin email: ")

try:
    with warnings.catch_warnings():
        warnings.simplefilter("error", getpass.GetPassWarning)
        password = getpass.getpass("Garmin password: ")
except getpass.GetPassWarning as error:
    raise SystemExit(
        "Cannot securely read your password in this console. "
        "Run this script from a terminal that supports hidden password input."
    ) from error

client = Garmin(
    email,
    password,
    prompt_mfa=lambda: input("MFA code: "),
)
client.login("~/.garminconnect")

token = pathlib.Path.home().joinpath(".garminconnect", "garmin_tokens.json").read_text()

print()
print("=" * 60)
print("SUCCESS! Copy everything between the lines below")
print("(the whole block, starting and ending with curly braces)")
print("=" * 60)
print(token)
print("=" * 60)
