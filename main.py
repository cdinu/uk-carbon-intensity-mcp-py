import argparse
import datetime
import sys

import requests
from fastmcp import FastMCP

mcp = FastMCP("CarbonIntensityMCP")


@mcp.tool(name="Get Current Intensity")
def intensity_current():
    """Fetches the current carbon intensity of the UK electricity grid.
    Returns a JSON with the current carbon intensity in gCO2eq/kWh."""
    url = "https://api.carbonintensity.org.uk/intensity"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["data"]

    except Exception as e:
        return f"Failed to retrieve current carbon intensity: {str(e)}"


@mcp.tool(name="Read Carbon Intensity for Dates and Postcode")
def intensity_for_dates_and_postcode(
    from_datetime: str,
    to_datetime: str,
    postcode: str,
):
    """Fetches electricity grid carbon intensity data for a specific UK postcode and time range.
    The `from_datetime` and `to_datetime` should be in ISO 8601 format (e.g. 2018-05-15T12:00Z).
    The `postcode` needs only the first part e.g. RG10 (without the last three characters or space)
    Returns a summary including average forecast and generation mix. Dates returned are UTC. Units are gCO2eq/kWh.
    """
    url = f"https://api.carbonintensity.org.uk/regional/intensity/{from_datetime}/{to_datetime}/postcode/{postcode}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]

    except Exception as e:
        return f"Failed to retrieve carbon intensity data: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="sse")
