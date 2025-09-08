#!/usr/bin/env python3
"""
Hugging Face Spaces app for UK Carbon Intensity MCP Server
This runs the MCP server using SSE transport for web deployment
"""
import os
import sys
from main import mcp

if __name__ == "__main__":
    # Force SSE transport for Hugging Face Spaces
    print("Starting UK Carbon Intensity MCP Server on Hugging Face Spaces", file=sys.stderr)
    print("Transport: SSE (Server-Sent Events)", file=sys.stderr)
    
    # Run the MCP server with SSE transport
    # FastMCP will handle the host/port configuration automatically
    mcp.run(transport="sse")
