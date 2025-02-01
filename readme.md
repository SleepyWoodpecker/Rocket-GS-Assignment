![image](assets/Grafana_task.png)

**Setup Instructions**

1. Install the following packages & verify that they have been installed

   1. Grafana | Verify installation using `grafana -v`

   2. Telegraf | Verify installation using `telegraf --version`

2. Run a python script to stream the desired data to the telegraf servers. The following commands correspond to the python scripts for the following tasks:

   1. (Basic Setup) Test with random data: `python Grafana_Backend/Grafana_Test_RandomVals.py`

   2. (Gaussian Data) Test with gaussian data: `python Grafana_Backend/Grafana_With_Gaussian.py`

   3. (Sinusoidal Data) Test with sinusoidal data: `python Grafana_Backend/Grafana_With_Sinusoidal.py`

   4. (New GUI) Test with 10 data sensors: `python Grafana_Backend/Grafana_With_Ten.py`

   5. (Hotfire data) Test with CSV files: `python Grafana_Backend/Grafana_From_CSV.py`

3. Start the granfana server and obtain a service account

   1. Mac: `brew services start grafana`

   2. Windows: Navigate to the installation path of grafana. File path should look something like: `GrafanaLabs/grafana/bin/grafana-server.exe`

   3. Navigate to `localhost:3000/org/serviceaccounts`

   4. Create a new service account with display name ‘admin’ and role admin

   5. Once created, click the ‘add service account token’ button

   6. Let the display name be ‘admin’ and COPY THE CODE DOWN!

4. Add your service account token to telegraf files

   1. inside the telegraf folder, modify line 10 of OctocouplerStates.conf, changing `Bearer *****` by replacing `****` with your Grafana admin code

   2. Do the same for SensorVals.conf

5. In separate **NEW TERMINAL WINDOWS**, cd into the telegraf folder & start the telegraf agents using the following commands

   1. Sensor readings: `telegraf --config telegraf/SensorVals.conf`

   2. Octocoupler: `telegraf --config telegraf/OctocouplerStates.conf`

6. To visualize your data on grafana, go to localhost:3000 on your browser and perform the following steps. Note: this requires you to have already run `brew services start grafana`

   1. Create a new service account
   2. Home > Dashboards > New dashboard > Import dashboard
   3. Choose the corresponding .json dashboard from /Grafana_Frontend, or build your own using the templates in Grafana_Frontend/template_panels
