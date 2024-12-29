![image](assets/Grafana_task.png)

**Setup Instructions**

1. Install the following packages & verify that they have been installed

   1. Grafana | Verify installation using `grafana -v`

   2. Telegraf | Verify installation using `telegraf --version`

2. Start the granfana server
   1. Mac: `brew services start grafana`

   2. Windows: Navigate to the installation path of grafana. File path should look something like: `GrafanaLabs/grafana/bin/grafana-server.exe`

4. In separate **NEW TERMINAL WINDOWS**, start the telegraf agents using the following commands

   1. Sensor readings: `telegraf --config Grafana_Files/OctocouplerStates.conf`

   2. Octocoupler: `telegraf --config Grafana_Files/OctocouplerStates.conf`

5. Run a python script to stream the desired data to the telegraf servers. The following commands correspond to the python scripts for the following tasks:

   1. (Basic Setup) Test with random data: `python Grafana_Files/Grafana_Test_RandomVals.py`

   2. (Gaussian Data) Test with gaussian data: `python Grafana_Files/Grafana_With_Gaussian.py`

   3. (Sinusoidal Data) Test with sinusoidal data: `python Grafana_Files/Grafana_With_Sinusoidal.py`

   4. (New GUI) Test with 10 data sensors: `python Grafana_Files/Grafana_With_Ten.py`

   5. (Hotfire data) Test with CSV files: `python Grafana_Files/Grafana_From_CSV.py`
