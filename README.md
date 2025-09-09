# UK Carbon Intensity MCP Server

A naive, didactic, Model Context Protocol (MCP) server that provides access to UK electricity grid carbon intensity data through the National Grid's Carbon Intensity API.

## What is this?

This is an MCP (Model Context Protocol) server that wraps the UK Carbon Intensity API, allowing AI assistants and other MCP clients to access:

- **Real-time carbon intensity data** for the UK electricity grid
- **Regional carbon intensity data** by postcode
- **Forecasted carbon intensity** for planning energy usage
- **Generation mix data** showing renewable vs fossil fuel sources

## How to use

This MCP server runs using Server-Sent Events (SSE) transport and can be connected to by MCP clients. The server provides the following tools:

### Available Tools

1. **get_current_intensity()** - Get the current UK grid carbon intensity
2. **get_carbon_intensity(from_datetime, to_datetime, postcode)** - Get historical/forecasted data for a specific region and time range

### API Endpoints

When running, the MCP server will be available at the base URL provided by Hugging Face Spaces, with MCP protocol endpoints for tool discovery and execution.

## Data Source

This implementation wraps the **UK Carbon Intensity API** provided by **National Energy System Operator (NESO)**:

- **Original API**: [carbonintensity.org.uk](https://carbonintensity.org.uk/)
- **API Documentation**: [carbon-intensity.github.io/api-definitions](https://carbon-intensity.github.io/api-definitions/)
- **Data Source**: National Grid Electricity System Operator (NESO)

## About Carbon Intensity

Carbon intensity measures how much CO2 is emitted per unit of electricity consumed (gCO2eq/kWh). Lower values indicate cleaner electricity from renewable sources, while higher values indicate more fossil fuel generation.

## Disclaimer

This project is an independent implementation and is not associated with, endorsed by, or affiliated with National Grid Electricity System Operator (NESO). It wraps their publicly available API for educational and development purposes.

## Technical Details

- **Framework**: FastMCP (Python MCP framework)
- **Transport**: Server-Sent Events (SSE)
- **Dependencies**: mcp[cli], requests, fastapi, uvicorn
- **Python Version**: >=3.13

For more information about this implementation, see: [cdi.nu/talks/2025-09-RSECon](https://cdi.nu/talks/2025-09-RSECon)
