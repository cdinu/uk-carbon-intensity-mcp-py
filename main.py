import argparse
import datetime
import sys

import requests
from fastmcp import FastMCP

mcp = FastMCP("CarbonIntensityMCP")


@mcp.tool()
def get_current_intensity():
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


@mcp.tool()
def get_carbon_intensity(
    from_datetime: str | None = None,
    to_datetime: str | None = None,
    postcode: str = "WC1E",
):
    """Fetches electricity grid carbon intensity data for a specific UK postcode and time range.
    The `from_datetime` and `to_datetime` should be in ISO 8601 format (e.g. 2018-05-15T12:00Z).
    The `postcode` needs only the first part e.g. RG10 (without the last three characters or space)

    If `from_datetime` or `to_datetime` are not provided, defaults are set to 2 hours ago and 2 hours in the future respectively.
    If postcode is not provided, defaults to "WC1E" -- UCL London.
    Returns a summary including average forecast and generation mix.
    """
    if from_datetime is None:  # default to 2 hours ago
        from_datetime = (
            datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=2)
        ).isoformat() + "Z"

    if to_datetime is None:  # default to 2 hours in the future
        to_datetime = (
            datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
        ).isoformat() + "Z"

    url = f"https://api.carbonintensity.org.uk/regional/intensity/{from_datetime}/{to_datetime}/postcode/{postcode}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]

    except Exception as e:
        return f"Failed to retrieve carbon intensity data: {str(e)}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Carbon Intensity MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="sse",
        help="Transport method: stdio for standard input/output or sse for server-sent events",
    )

    args = parser.parse_args()

    print(f"Using transport: {args.transport}", file=sys.stderr)
    if args.transport == "sse":
        mcp.run(transport="sse")
    else:
        mcp.run()
