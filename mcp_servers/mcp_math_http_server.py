from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings


mcp: FastMCP = FastMCP(
    "MathLearningServer",
    host="127.0.0.1",
    port=8001,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False
    ),
)


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def subtract_numbers(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide_numbers(a: float, b: float) -> str:
    """Divide a by b. Returns an error if b is 0."""
    if b == 0:
        return "Error: division by zero is not allowed."
    return str(a / b)


@mcp.tool()
def factorial(n: int) -> str:
    """Return n! for non-negative integers."""
    if n < 0:
        return "Error: factorial is only defined for n >= 0."

    result = 1
    for i in range(2, n + 1):
        result *= i
    return str(result)


if __name__ == "__main__":
    mcp.run(transport="sse")
