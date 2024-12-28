![image](assets/Grafana_task.png)

**Setup Instructions**

1. Install the following packages & verify that they have been installed
   a. Grafana | Verify installation using `grafana -v`
   b. Telegraf | Verify installation using `telegraf --version`
2. On Mac, start the grafana server using `brew services start grafana`
3. In separate **new terminal windows**, start the telegraf agents using the following commands
   a. Sensor readings: `telegraf --config Grafana_Files/OctocouplerStates.conf`
   b. Octocoupler: `telegraf --config Grafana_Files/OctocouplerStates.conf`
4. Run the python script to stream data to the telegraf server. The following commands correspond to the python scripts for the following tasks:
   a. (Task 1) Test with random data: `python Grafana_Files/Grafana_Test_RandomVals.py`
   b. (Task 2) Test with gaussian data: `python Grafana_Files/Grafana_With_Gaussian.py`
   c. (Task 2) Test with sinusoidal data: `python Grafana_Files/Grafana_With_Sinusoidal.py`
   d. (Task 3) Test with 10 data sensors: `python Grafana_Files/Grafana_With_Ten.py`
   e. (Bonus) Test with CSV files: `python Grafana_Files/Grafana_From_CSV.py`
