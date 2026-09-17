import requests

#***********************************
# Authentication part
#***********************************
url = "https://restful-booker.herokuapp.com/auth"

# credentials as json
credentials ={
    "username":"admin",
    "password": "password123"
}

response = requests.post(url, json=credentials)

# Getting token
token = None
is_token = False
if response.status_code == requests.codes.ok:
    token = response.json().get("token")

    if token:
        print(f"Token received",token)
        is_token = True
    else:
        print("Authentication succeeded, but no token was returned.")
else:
    print("Authentication unsuccessful.")


#***********************************
# Updating part
#***********************************
booking_id = 1
url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"

# Json as per the documentation
updated_data = {
    "firstname": "Salar",
    "lastname": "Bond",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-01-01",
        "checkout": "2026-01-02"
    }
}

# Adding the token to the header as a Cookie, as per the documentation
headers = {
    "Cookie":f"token={token}",
    "Content-Type":"application/json"
}
# Update record
if is_token:
    res = requests.put(url, json=updated_data, headers=headers)

    if res.status_code == requests.codes.ok:
        print(res.status_code)
        print(res.text)
    else:
        print(res.status_code)
        print(res.text)

#***********************************
# Verify the updated booking
#***********************************

url = "https://restful-booker.herokuapp.com/booking/1"

parameters = {
    "firstname": "Salar"
}

headers = {
   "Accept": "application/json"
}

res1 = requests.get(url, headers=headers)

print("\nVerification:")
print(res1.status_code)
print(res1.json())