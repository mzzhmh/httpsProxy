#!/usr/bin/python3.6
from flask import Flask,jsonify,request,Response
import requests
import json
import sys

if(len(sys.argv)<3):
  print("USAGE: python3.6 app.py IP SiteNumPort (e.g., python3.6 app.py 10.49.9.220 3080)",file=sys.stderr)
  sys.exit(1)
IP=sys.argv[1]
Siteport=sys.argv[2]

print(IP,file=sys.stderr)
print(Siteport,file=sys.stderr)

aggregateURL="https://"+IP+"/api/meters/aggregates"
soeURL="https://"+IP+"/api/system_status/soe"
gridStatusURL="https://"+IP+"/api/system_status/grid_status"
siteMasterURL="https://"+IP+"/api/sitemaster"

app = Flask(__name__)


@app.route('/aggregates')
def get_aggregates():
  print("\n1############# GET aggregates REQUEST ###########",file=sys.stderr)
  try:
    aggResp = requests.get(aggregateURL,verify=False,timeout=30)
    if (aggResp.status_code == 200):
      #add the connection flag tag
      jsonData = json.loads(aggResp.text) 
      jsonData["API_Server_Error"]=0
      print("[AGG]:"+json.dumps(jsonData),file=sys.stderr)
      ret = json.dumps(jsonData)
      sys.stdout.flush()
      return Response(ret,status=200)
    else:
      print("[AGG]:"+aggResp.text,file=sys.stderr)
      ret = '{"API_Server_Error":1}'
      print("[AGG]:"+ret,file=sys.stderr)
      sys.stdout.flush()
      return Response(ret,status=200)
  except Exception as e:
    print("[AGG]:"+str(e),file=sys.stderr)
    ret = '{"API_Server_Error":1}'
    print("[AGG]:"+ret,file=sys.stderr)
    sys.stdout.flush()
    return Response(ret,status=200)
  print("############## END aggregates REQUEST ###########\n",file=sys.stderr)
  

@app.route('/sitemaster')
def get_sitemaster():
  print("\n1############# GET sitemaster REQUEST ###########",file=sys.stderr)
  try:
    aggResp = requests.get(siteMasterURL,verify=False,timeout=30)
    if (aggResp.status_code == 200):
      #add the connection flag tag
      jsonData = json.loads(aggResp.text) 
      jsonData["API_Server_Error"]=0
      print("[SMT]:"+json.dumps(jsonData),file=sys.stderr)
      ret = json.dumps(jsonData)
      sys.stdout.flush()
      return Response(ret,status=200)
    else:
      print("[SMT]:"+aggResp.text,file=sys.stderr)
      ret = '{"API_Server_Error":1}'
      print("[SMT]:"+ret,file=sys.stderr)
      sys.stdout.flush()
      return Response(ret,status=200)
  except Exception as e:
    print("[SMT]:"+str(e),file=sys.stderr)
    ret = '{"API_Server_Error":1}'
    print("[SMT]:"+ret,file=sys.stderr)
    sys.stdout.flush()
    return Response(ret,status=200)
  print("############## END sitemaster REQUEST ###########\n",file=sys.stderr)


@app.route('/grid_status')
def get_gridStatus():
  print("\n1############# GET grid_status REQUEST ###########",file=sys.stderr)
  try:
    aggResp = requests.get(gridStatusURL,verify=False,timeout=30)
    if (aggResp.status_code == 200):
      #add the connection flag tag
      jsonData = json.loads(aggResp.text) 
      jsonData["API_Server_Error"]=0
      print("[GRD]:"+json.dumps(jsonData),file=sys.stderr)
      ret = json.dumps(jsonData)
      sys.stdout.flush()
      return Response(ret,status=200)
    else:
      print("[GRD]:"+aggResp.text,file=sys.stderr)
      ret = '{"API_Server_Error":1}'
      print("[GRD]:"+ret,file=sys.stderr)
      sys.stdout.flush()
      return Response(ret,status=200)
  except Exception as e:
    print("[GRD]:"+str(e),file=sys.stderr)
    ret = '{"API_Server_Error":1}'
    print("[GRD]:"+ret,file=sys.stderr)
    sys.stdout.flush()
    return Response(ret,status=200)
  print("############## END grid_status REQUEST ###########\n",file=sys.stderr)

@app.route('/soe')
def get_soe():
  print("\n1############# GET soe REQUEST ###########",file=sys.stderr)
  try:
    aggResp = requests.get(soeURL,verify=False,timeout=30)
    if (aggResp.status_code == 200):
      #add the connection flag tag
      jsonData = json.loads(aggResp.text) 
      jsonData["API_Server_Error"]=0
      print("[SOE]:"+json.dumps(jsonData),file=sys.stderr)
      ret = json.dumps(jsonData)
      sys.stdout.flush()
      return Response(ret,status=200)
    else:
      print("[SOE]:"+aggResp.text,file=sys.stderr)
      ret = '{"API_Server_Error":1}'
      print("[SOE]:"+ret,file=sys.stderr)
      sys.stdout.flush()
      return Response(ret,status=200)
  except Exception as e:
    print("[SOE]:"+str(e),file=sys.stderr)
    ret = '{"API_Server_Error":1}'
    print("[SOE]:"+ret,file=sys.stderr)
    sys.stdout.flush()
    return Response(ret,status=200)
  print("############## END soe REQUEST ###########\n",file=sys.stderr)


if __name__ == '__main__':
    app.run(host='10.236.76.132',port=Siteport)
