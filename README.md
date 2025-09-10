# UK Carbon Intensity MCP Server

A naive, didactic, Model Context Protocol (MCP) server that provides access to UK electricity grid carbon intensity data through the National Grid's Carbon Intensity API.

## Data Source

This implementation wraps the **UK Carbon Intensity API** provided by **National Energy System Operator (NESO)**:

- **Original API / Data Source**: [carbonintensity.org.uk](https://carbonintensity.org.uk/)
- **API Documentation**: [carbon-intensity.github.io/api-definitions](https://carbon-intensity.github.io/api-definitions/)

## About Carbon Intensity

Carbon intensity measures how much CO2 is emitted per unit of electricity consumed (gCO2eq/kWh). Lower values indicate cleaner electricity from renewable sources, while higher values indicate more fossil fuel generation.

## Disclaimer

This project is an independent implementation and is not associated with, endorsed by, or affiliated with National Grid Electricity System Operator (NESO).

## Technical Details

- **Framework**: FastMCP (Python MCP framework)
- **Transport**: Server-Sent Events (SSE)

For more information about this implementation, see: [cdi.nu/talks/2025-09-RSECon](https://cdi.nu/talks/2025-09-RSECon)
