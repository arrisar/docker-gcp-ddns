import pathlib
import subprocess
import requests
import time
import yaml


def readConfig():
  try:
    with open("/app/data/config.yaml") as config:
      return yaml.load(config, Loader=yaml.BaseLoader)

  except (FileNotFoundError):
    subprocess.call("cp /app/config.default.yaml /app/data/config.yaml", shell=True)


def updateRecords(records, ip):
  for record in records:
    command = f"gcloud beta dns record-sets update {record['name']} --zone={record['zone']} --type={record['type']} --ttl={record['ttl']} --rrdatas={ip}"
    subprocess.call(command, shell=True)


def run():
  config = readConfig()

  auth = config['auth']
  subprocess.call(f"gcloud auth activate-service-account {auth['account']} --key-file={auth['key']}  --project={auth['project']}", shell=True)

  current = False
  while True:
    result = requests.get('https://api.ipify.org').text
    
    if current != result:
      current = result
      updateRecords(config["records"], result)
    
    time.sleep(5)


run()