# WPMCP

WPMCP aims to provide a **Management Control Panel (MCP)** server for automating administrative WordPress tasks through the WordPress REST API. The server is written in Python and acts as a central interface for managing multiple WordPress installations.

## Objectives

- Offer a simple RESTful service that wraps WordPress operations such as plugin management, user administration and site configuration.
- Use the standard WordPress REST API so administrators can integrate with existing sites without additional plugins.
- Provide secure authentication options that fit a variety of WordPress setups.

## Installation

### Requirements

- Python 3.12 or newer
- `requests` and any other dependencies listed in `requirements.txt`

Install the required packages:

```bash
python3 -m pip install -r requirements.txt
```

### Initial setup

1. Clone this repository.
2. Install dependencies as above.
3. Prepare configuration for your WordPress instances (to be defined in future versions).

Once these steps are complete you will be ready to run the MCP server (implementation forthcoming).

## Running the server

The server is implemented with **FastAPI**. Set the following environment variables
before starting:

```
WP_BASE_URL=<https://your-wordpress-site>
WP_API_KEY=<your-api-key>
```

Install dependencies as shown above and run:

```bash
uvicorn wpmcp.server:app --reload
```

This starts the MCP server locally. Endpoints such as `POST /posts` will create
posts on the configured WordPress instance using the API key for authentication.

## WordPress REST API overview

WordPress exposes most administrative functionality through its REST API at `/wp-json/wp/v2/`. It supports actions like retrieving posts, managing users and installing plugins. For this MCP server, the API will be leveraged to perform administrative tasks automatically.

### Authentication methods

Several authentication approaches can be used with the WordPress REST API:

1. **Cookie authentication** – relies on WordPress login cookies and is mainly suited for browser-based clients.
2. **Application passwords** – built-in feature enabling basic authentication using a generated password per user. Works over HTTPS and is simple to integrate.
3. **OAuth or JWT plugins** – third-party plugins offer OAuth 1.0a, OAuth2 or JWT token authentication when more robust solutions are required.

Depending on your environment you can pick whichever method suits your security and automation needs.

