# SNR Analyzer

Hi, I wrote some python scripts to get the Line Rate, SNR and Attenuation from my router.

Then I put these scripts on my crontab to gather these data every 1 minute.

### How to run
1. Rename `data.csv.sample` to `data.csv` for example data.
2. Rename `chart.sample` to `chart` for chart scripts.
3. Install packages if you have'nt alreadly `pip install -r requirements.txt`
4. run `python app.py` or `python make-chart.py`

### Compatibility
To run on your environment you might need to edit `app.py` bs4 parts to select data from your own router and put your auth info there too.

You can use `make-chart.py` to create plot charts based on that data.

Chart examples:

| Downstream Rate | Upstream Rate |
| --- | --- |
| ![Downstream Rate](chart.sample/20200226-031844/Downstream%20Rate.jpg) | ![Upstream Rate](chart.sample/20200226-031844/Upstream%20Rate.jpg) |

| Downstream SNR | Upstream SNR |
| --- | --- |
| ![Downstream SNR](chart.sample/20200226-031844/Downstream%20SNR.jpg) | ![Upstream SNR](chart.sample/20200226-031844/Upstream%20SNR.jpg) |

| Downstream Attenuation | Upstream Attenuation |
| --- | --- |
| ![Downstream Attenuation](chart.sample/20200226-031844/Downstream%20Attenuation.jpg) | ![Upstream Attenuation](chart.sample/20200226-031844/Upstream%20Attenuation.jpg) |
