"""
NAG (Network Advisor Gateway) — Standalone Demo & API Server
100% Headless / Function-First (Users can plug in their own UI or use as Middleware).
"""
from fastapi import FastAPI, Request
from nag_engine import NAGSecurityMiddleware, build_nag_a2a_packet

app = FastAPI(
    title="NAG - Network Advisor Gateway (AI-to-AI Security Engine)",
    description="Defensive AI-to-AI Ethical & Stealth Interception Gateway against Autonomous Hacking Agents.",
    version="1.0.0"
)

# Attach NAG Middleware in 1 line
app.add_middleware(NAGSecurityMiddleware)


@app.get("/")
def root():
    return {
        "service": "NAG (Network Advisor Gateway)",
        "status": "active",
        "mode": "AI-to-AI Symbolic & Neural Stealth Interception",
        "docs": "/docs",
        "test_endpoint": "/nag/simulate-probe"
    }


@app.get("/nag/simulate-probe")
def simulate_probe(request: Request, target: str = "/.env.production"):
    """
    Test endpoint to preview the exact A2A Universal Packet sent to an attacking AI agent.
    """
    client_ip = request.client.host if request.client else "127.0.0.1"
    return build_nag_a2a_packet(client_ip, target)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8099, reload=False)

