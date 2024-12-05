"""
WSGI configuration file for the Flask application.

This module sets up the WSGI application with proper proxy handling and server configuration.
It configures the application to work behind a proxy server by handling X-Forwarded-* headers
and sets up the development server with multi-threading and multiple worker processes when
run directly.

The configuration includes:
- ProxyFix middleware for proper proxy header handling
- Multi-threading support
- 3 worker processes
- Listening on all network interfaces
- Running on port 8000
"""

# Import the Flask application instance from app.py
from app import app
# Import ProxyFix middleware to handle proxy server headers
from werkzeug.middleware.proxy_fix import ProxyFix

# Apply ProxyFix middleware to handle X-Forwarded-* headers when behind a proxy
app.wsgi_app = ProxyFix(app.wsgi_app)

# Only run the application directly if this file is executed
if __name__ == "__main__":
    # Start the Flask development server with the following configuration:
    app.run(
        threaded=True,     # Enable multi-threading for handling concurrent requests
        processes=3,       # Run with 3 worker processes for better performance
        host='0.0.0.0',   # Listen on all available network interfaces
        port=8000         # Run the server on port 8000
    )
