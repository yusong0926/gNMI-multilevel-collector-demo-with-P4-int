#  OPENCONFIG POC 

## OBJECTIVE 
Assess open config's viability for a-cord.
Demo presenttion on cord build (starts on 16:28)
https://www.youtube.com/watch?v=RCrlbSiN9eY&list=PLCnPGaNt7C5fsU4n67baCbLRMJiBQjVq8&index=4

## Get STARGED
### Install Dependencies
Install dependencies: pip, grpc, potsdb, grafana
```
sudo apt install python-pip

pip install -r requirements.txt
```
### OPENTSDB
The address and port of OPENSTDB is defined in test_client.py. The default is localhost:4242. You can change it in test_client.py. Metric name will be the path name you subscribed.
```sh
docker run -p 4242:4242 petergrace/opentsdb-docker
```
### Grafana 
The default port is localhost:3000. Default UI login username: admin, password: admin.
UI: http://hostip:3000
```sh
docker run -d --name=grafana -p 3000:3000 grafana/grafana
```
### Start Probe Server
```
cd app/probe
python probe.py --port 7000 --time 0.01
```
probe server will run in port 7000, probe will simulate p4 in-band telemetry and update in every 0.01 second when a subscription request received.

Use -h to check the argument options
### Start Collector Server 
```sh
cd app/collector
python collector.py --port 7001 --device_port 7000 --sample 1 
```
collector server will run in port 7001, it will subscribe to port 7000 which is the probe server. How many updates will be aggregated is specifyed by sample argument.
You can run mutiple collectors or create a collecotr chain by configuring the port and device port.

Use -h to check the argument options
### Start Test_client 
```sh
cd app/test-client
python test_client.py --subscribe "p4_int" --port 7001
```
test_client will subscribe to port 7001 which is the collector server, and publish the datat to openTSDB.

Use -h to check the argument options
``
