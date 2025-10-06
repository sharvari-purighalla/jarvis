# import shim for different SDK layouts
try:
    from mcp import tool                   # current SDK
except ImportError:
    try:
        from mcp.server.decorators import tool   # older SDKs
    except Exception:
        # Some distributions publish under model_context_protocol
        from mcp import tool
