#  OPENCONFIG POC 

## OBJECTIVE 
Assess open config's viability for a-cord

## Get STARGED
install dependencies: grpc, potsdb
'''
pip install -r requirements.txt
'''
### Start Probe Server
```
python probe.py --port 80049 --time 0.01
```
probe server will run in port 80049, probe will generate updates in every 0.01 second when a subscription request received.

Use -h to check the argument options
### Start Collector Server 
```sh
python collector.py --port 80050 --device_port 80049 --sample 1 
```
collector server will run in port 80050, it will subscribe to port 80049 which is the probe server. How many updates will be aggregated is specifyed by sample argument.
You can run mutiple collectors or create a collecotr chain by configuring the port and device port.

Use -h to check the argument options
### Start Test_client 
```sh
python test_client.py --subscribe "interfaces/ethnet/state" --port 80050
```
test_client will subscribe to port 80050 which is the collector server, and send request for updates of path: "interfaces/ethnet/state"

Use -h to check the argument options
### OPENTSDB
The address and port of OPENSTDB is defined in test_client.py. The default is localhost:4242. You can change it in test_client.py. Metric name will be the path name you subscribed.

