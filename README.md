# Country Boundary GeoJSON

The repo contains coastline and land boundaries for UK, Ireland, Germany, Greece, Finland, Bulgaria, Hungary, Malta, and Italy along with the python script to generate it. The data is generated using the geojson files at https://github.com/simonepri/geo-maps. The script fetches the world coastline and land boundaries, processes it and outputs a combined geojson for required countries. Resolution and the countries can be configured in the script.

## Requirements

The script needs requests library to run, before running the script install the requirements by running

```bash
pip install requests
```

## Running the script

```bash
python process.py
```
