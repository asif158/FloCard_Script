# Load Time Checker and Dashboard for Website

This Python script `loadtest.py` checks the load time of multiple URLs and visualizes the results using Plotly. Additionally, there is a script `extract.py` which extracts the links available on the URL provided inside the code and creates a text file containing all the links.

## Description

The script `loadtest.py` performs the following tasks:

- Iterates over a list of URLs.
- Checks the load time for each URL using the `requests` library.
- Updates a dashboard with the load times using `plotly.express`.
- Displays a bar chart where successful loads are represented by green bars and failed loads are indicated with red annotations.

The script `extract.py` performs the following tasks:

- Extracts all the links available on URLs.
- Create a text file having the URLs.

## Requirements

Ensure you have Python 3.x installed along with the following packages:

- `requests`
- `plotly`
- `pandas`

You can install these dependencies using `pip` and the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the script (`loadtest.py`).

2. Install the required dependencies using the command above.

3. Modify `base_url` and `endpoints` in `loadtest.py` to include the URLs you want to check.

4. Run the script:

   ```bash
   python loadtest.py
   ```

5. The script will output the load times for each URL to the console and automatically open a dashboard using Plotly in the default web browser.

## Notes

- Ensure your environment has internet access to fetch the URLs.
- Customize the script as needed for your specific use case or website URLs.
