# 1 What is a Web API?
"""A Web API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate over the web, typically using HTTP. It defines endpoints, request/response formats, and authentication methods."""

# 2 How does a Web API differ from a web service?
"""All web services are APIs, but not all web APIs are web services. Web services specifically use SOAP, XML, or REST over HTTP and are designed for machine-to-machine interaction. Web API is a broader term that includes any API exposed over the web, including lightweight RESTful services and WebSockets."""

# 3 What are the benefits of using Web APIs in software development?
"""Benefits include: platform independence (any client can connect), reusability, scalability, loose coupling between systems, easier integration with third-party services, improved maintainability, and support for multiple data formats (JSON, XML)."""

# 4 Explain the difference between SOAP and RESTful APIs.
"""SOAP (Simple Object Access Protocol) is a protocol with strict standards, uses XML, and provides built-in error handling and security. REST (Representational State Transfer) is an architectural style that uses HTTP methods, supports multiple formats (JSON, XML), and is lighter, stateless, and more cache-friendly."""

# 5 What is JSON and how is it commonly used in Web APIs?
"""JSON (JavaScript Object Notation) is a lightweight text format for data interchange. It is easy to read/write and language-agnostic. Web APIs commonly use JSON in request bodies and responses because it is compact, fast to parse, and works seamlessly with JavaScript."""

# 6 Can you name some popular Web API protocols other than REST?
"""Yes: GraphQL (query language for APIs), gRPC (high-performance RPC using Protocol Buffers), SOAP (XML-based protocol), WebSockets (real-time bidirectional communication), and MQTT (IoT lightweight messaging)."""

# 7 What role do HTTP methods (GET, POST, PUT, DELETE, etc.) play in Web API development?
"""HTTP methods define the intended action on a resource: GET retrieves data, POST creates a new resource, PUT replaces an entire resource, PATCH partially updates, DELETE removes a resource. They make APIs predictable and align with CRUD operations."""

# 8 What is the purpose of authentication and authorization in Web APIs?
"""Authentication verifies the identity of the client (who you are). Authorization determines what resources and actions the authenticated client is allowed to access (what you can do). Both are critical for security, preventing unauthorised access and data breaches."""

# 9 How can you handle versioning in Web API development?
"""Common versioning strategies: URI path (/v1/users), custom request header (Accept: version=1.0), query parameter (?version=1), or content negotiation. Versioning allows backward-compatible changes and smooth transitions for API consumers."""

# 10 What are the main components of an HTTP request and response in the context of Web APIs?
"""HTTP request components: method (GET, POST), URL, headers (Content-Type, Authorization), and optional body. HTTP response components: status code (200, 404), headers, and optional body (e.g., JSON data)."""

# 11 Describe the concept of rate limiting in the context of Web APIs.
"""Rate limiting restricts the number of API requests a client can make within a given time window (e.g., 1000 requests per hour). It prevents abuse, ensures fair usage, protects server resources, and improves overall stability."""

# 12 How can you handle errors and exceptions in Web API responses?
"""Use standard HTTP status codes (4xx for client errors, 5xx for server errors) and return a consistent error object containing an error code, message, and optional details. Avoid exposing stack traces. Validate inputs and return meaningful messages."""

# 13 Explain the concept of statelessness in RESTful Web APIs.
"""Statelessness means each request from client to server must contain all the information needed to understand and process it. The server does not store any client context between requests. This improves scalability, reliability, and visibility."""

# 14 What are the best practices for designing and documenting Web APIs?
"""Best practices: use RESTful conventions, meaningful resource names, proper HTTP methods, versioning, standard status codes, pagination, filtering, rate limiting, security (HTTPS, authentication). Document using OpenAPI (Swagger) or similar tools."""

# 15 What role do API keys and tokens play in securing Web APIs?
"""API keys identify the project or application, while tokens (like JWT) carry identity and authorisation claims. They are used for authentication and access control, often together with rate limiting. Tokens can be short-lived and scoped."""

# 16 What is REST, and what are its key principles?
"""REST (Representational State Transfer) is an architectural style for designing networked applications. Key principles: client-server separation, statelessness, cacheability, layered system, uniform interface (resources identified by URIs, representations), and code-on-demand (optional)."""

# 17 Explain the difference between RESTful APIs and traditional web services.
"""Traditional web services (SOAP) are protocol-driven, rely on XML, and include WSDL contracts. RESTful APIs are resource-oriented, use HTTP methods, support multiple formats (JSON, XML), are lighter, stateless, and easier to consume from browsers."""

# 18 What are the main HTTP methods used in RESTful architecture, and what are their purposes?
"""GET – retrieve a resource; POST – create a new resource; PUT – completely replace a resource; PATCH – partial update; DELETE – remove a resource; HEAD – retrieve headers only; OPTIONS – discover allowed methods."""

# 19 Describe the concept of statelessness in RESTful APIs.
"""Statelessness mandates that every HTTP request from client to server must contain all necessary information (authentication, parameters, etc.). The server does not remember previous interactions. This simplifies server design and improves horizontal scaling."""

# 20 What is the significance of URIs (Uniform Resource Identifiers) in RESTful API design?
"""URIs uniquely identify each resource (e.g., /users/123). They should be nouns (not verbs), hierarchical, predictable, and follow a consistent naming convention. Good URIs make the API self-descriptive and easy to understand."""

# 21 Explain the role of hypermedia in RESTful APIs. How does it relate to HATEOAS?
"""Hypermedia (links) in responses tells clients what actions are possible next. HATEOAS (Hypermedia As The Engine Of Application State) is a REST constraint: the server provides links dynamically, so clients navigate the API without hard-coded URLs, enabling decoupled evolution."""

# 22 What are the benefits of using RESTful APIs over other architectural styles?
"""Benefits: simplicity (HTTP), scalability (stateless), performance (caching), flexibility (multiple formats), loose coupling, wide tooling support, human‑readable URLs, and natural mapping to CRUD operations."""

# 23 Discuss the concept of resource representations in RESTful APIs.
"""Resources are abstract entities (e.g., 'user'). A representation is the actual data format (JSON, XML, etc.) returned or sent. Different representations of the same resource can be requested via the Accept header. Representations include data and metadata (links)."""

# 24 How does REST handle communication between clients and servers?
"""REST uses HTTP as the communication protocol. Clients send requests to server endpoints (URIs) with methods and bodies; servers respond with status codes and resource representations. Communication is stateless and each request is independent."""

# 25 What are the common data formats used in RESTful API communication?
"""The most common format is JSON (lightweight, easy to parse). Other formats include XML (verbose, used in SOAP), YAML (configuration), HTML (for hypermedia APIs), and plain text. JSON is preferred for modern REST APIs."""

# 26 Explain the importance of status codes in RESTful API responses.
"""Status codes communicate the result of an HTTP request in a standardised way: 2xx (success), 3xx (redirection), 4xx (client error, e.g., 404 Not Found), 5xx (server error). They help clients handle responses programmatically."""

# 27 Describe the process of versioning in RESTful API development.
"""Versioning can be done via URI (/v1/resource), custom header (Accept-Version), or query parameter. The API should support multiple versions concurrently for a transition period, deprecate old versions with clear timelines, and document changes."""

# 28 How can you ensure security in RESTful API development? What are common authentication methods?
"""Use HTTPS, validate inputs, implement rate limiting, and sanitise outputs. Common authentication methods: API keys, HTTP Basic Auth, OAuth 2.0, JWT (Bearer tokens), and OpenID Connect. Authorize users based on roles and scopes."""

# 29 What are some best practices for documenting RESTful APIs?
"""Use OpenAPI (Swagger) to generate interactive docs. Include endpoint descriptions, sample requests/responses, status codes, authentication details, error codes, rate limits, and versioning strategy. Keep docs up‑to‑date and versioned alongside the API."""

# 30 What considerations should be made for error handling in RESTful APIs?
"""Use appropriate HTTP status codes, return consistent error JSON (e.g., { 'error': { 'code': 400, 'message': 'Invalid user id' } }), provide actionable messages, log errors server‑side, and never expose stack traces or internal details."""

# 31 What is SOAP, and how does it differ from REST?
"""SOAP is a protocol that uses XML messaging, WSDL contracts, and often HTTP or SMTP. It is more rigid, supports ACID transactions, and has built‑in security (WS‑Security). REST is an architectural style, lighter, stateless, and uses JSON/XML over HTTP."""

# 32 Describe the structure of a SOAP message.
"""A SOAP message is an XML document containing: Envelope (root), Header (optional – metadata, security), Body (mandatory – request/response data), and optional Fault (error details). It follows strict XML schemas."""

# 33 How does SOAP handle communication between clients and servers?
"""Client sends a SOAP XML request (usually via HTTP POST) to a web service endpoint. Server processes the request and returns a SOAP XML response. Communication can also use SMTP, JMS, or TCP. WSDL defines the contract."""

# 34 What are the advantages and disadvantages of using SOAP-based web services?
"""Advantages: built‑in error handling (Fault), security (WS‑Security), ACID transactions, language/transport independence. Disadvantages: heavy XML payloads, slower performance, steep learning curve, less browser‑friendly, and more complex to implement."""

# 35 How does SOAP ensure security in web service communication?
"""SOAP uses WS‑Security (part of the SOAP standard) for encryption, digital signatures, and security tokens. It can also rely on transport‑level security (HTTPS). WS‑Security allows end‑to‑end message security beyond point‑to‑point TLS."""

# 36 What is Flask, and what makes it different from other web frameworks?
"""Flask is a lightweight, micro‑web framework for Python. It differs from full‑stack frameworks (like Django) by being minimalistic, giving developers freedom to choose libraries (ORM, forms, authentication), and providing only the essentials: routing, request/response handling, and Jinja2 templating."""

# 37 Describe the basic structure of a Flask application.
"""A basic Flask app consists of a Python script that creates a Flask instance, defines routes with decorators (@app.route), and runs the server. The structure can later grow to include templates (HTML), static files (CSS/JS), and blueprints for modularity."""

# 38 How do you install Flask on your local machine?
"""Using pip: `pip install flask`. It is recommended to create a virtual environment first (`python -m venv venv`, then activate it) to avoid conflicts. Optionally use `pipenv` or `poetry`."""

# 39 Explain the concept of routing in Flask.
"""Routing maps URLs to Python functions (view functions). Using `@app.route('/path')` decorator, Flask calls the associated function when that URL is requested. Routes can capture variable parts (e.g., `/user/<name>`), support HTTP methods, and generate dynamic responses."""

# 40 What are Flask templates, and how are they used in web development?
"""Templates are HTML files that contain placeholders and logic (Jinja2 syntax). They separate presentation from business logic. Flask renders templates using `render_template('index.html', name=user)`. This allows dynamic HTML generation, inheritance, and reusable components."""


# ------------------------------
# Optional: Print all Q&A neatly
# ------------------------------
def main():
    import ast
    import inspect

    # Extract all comment+docstring pairs from this file
    with open(__file__, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    qa_list = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('#') and not line.startswith('#!'):
            # Question line
            q_text = line.lstrip('#').strip()
            # Look ahead for a triple-quoted string
            if i+1 < len(lines):
                next_line = lines[i+1].strip()
                if next_line.startswith('"""') or next_line.startswith("'''"):
                    # Multi-line docstring
                    docstring = ''
                    i += 1
                    # Handle possible multi-line docstring
                    if lines[i].strip().startswith('"""'):
                        # Single line docstring
                        docstring = lines[i].strip().strip('"').strip("'")
                        i += 1
                    else:
                        # Multi-line
                        start_quote = lines[i].strip()[0:3]
                        end_quote = start_quote
                        doc_lines = []
                        while i < len(lines):
                            doc_lines.append(lines[i].rstrip())
                            if lines[i].rstrip().endswith(end_quote):
                                break
                            i += 1
                        docstring = '\n'.join(doc_lines).strip(start_quote).strip(end_quote).strip()
                        i += 1
                    qa_list.append((q_text, docstring))
                    continue
        i += 1

    # Print numbered results
    for idx, (q, a) in enumerate(qa_list, 1):
        print(f"{idx}. {q}")
        print(f"   {a}\n")

if __name__ == "__main__":
    main()