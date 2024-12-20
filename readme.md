**Getting GUI Running**

1. After looking through `Grafana_Files`, I have established that I should be using `Grafana_Test_ConstVals.py` or `Grafana_Test_RandomVals.py` to send data to the telegraf server, since these are the files that do not require reading data from a serial port
2. I also need to install the following packagaes:
   a. Grafana
   b. Telegraf
   c. Influx DB
3. I also need to set up a websocket for telegraf to communicate with grafana.
   a. For this, I referred to this tutorial: https://grafana.com/tutorials/stream-metrics-from-telegraf-to-grafana/
   b. Because the use of an API token is outdated, I used a service account's token instead
   c. Given this websocket url: `ws://localhost:3000/api/live/push/prometheus_ground_sys`, the channel to read from is: `stream/prometheus_ground_sys/\<header of influx string\>`
