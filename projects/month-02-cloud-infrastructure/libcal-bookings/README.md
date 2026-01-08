# LibCal Room Bookings Dashboard

A production web application providing real-time meeting room booking information for library staff at Lebanon Public Libraries.

## Problem Statement

Library custodians needed to check multiple systems at the end of their shifts to determine if after-hours meeting room bookings required them to stay late. Desk staff fielded frequent patron questions about room availability across multiple locations. Both workflows involved manual checking of LibCal's booking system, creating inefficiency and potential for missed information.

## Solution

A responsive web dashboard that:
- Displays bookings for 6 meeting rooms across 2 library branches
- Highlights after-hours bookings requiring custodian attention
- Provides quick room-switching for desk staff assisting patrons
- Automatically refreshes booking data every 15 minutes
- Integrates seamlessly with existing staff intranet

![Desktop View](../../../docs/screenshots/libcal-bookings-desktop.png)
![Mobile View-1](../../../docs/screenshots/libcal-bookings-mobile-1.png)
![Mobile View-2](../../../docs/screenshots/libcal-bookings-mobile-2.png)

## Technical Architecture

### Application Stack
- **Backend**: Python Flask application with modular route design
- **Frontend**: HTMX for dynamic content updates, Alpine.js for UI interactions
- **Data Source**: LibCal API (OAuth 2.0 authentication)
- **Containerization**: Docker with multi-stage builds
- **Web Server**: nginx reverse proxy
- **Automation**: systemd timers for scheduled data fetching

### Design Decisions

**Separation of Concerns**
- Flask routes decoupled from URL structure (nginx handles `/api/bookings` prefix)
- Hugo static site manages page structure, Flask provides dynamic booking data
- Separate routes for user-initiated refresh vs. automated fetching

**State Management**
- HTMX out-of-band swaps update timestamp and refresh button without full page reload
- Flask request context enables clean function composition without parameter passing
- Named Docker volumes persist booking data across container restarts

**Responsive Design**
- Desktop: Vertical room navigation with grouped branches (Kilton/Lebanon)
- Mobile: Dropdown selector with branch optgroups
- Shared card-based booking display optimized for quick scanning

## Key Features

### After-Hours Detection
Custodians see immediate visual alerts for bookings extending past cutoff hours:
- Monday-Thursday: 6:00 PM
- Friday-Saturday: 5:00 PM  
- Sunday: No after-hours bookings

### Booking Notes
Staff-only internal notes displayed via Alpine.js toggle:
- Hide complexity from quick-scan workflows
- Preserve detailed information when needed
- Multiple notes per booking with timestamps

### Multi-Room Support
Six rooms across two branches with intelligent filtering:
- Community Room, Conference Room, Tutorial Room (Kilton)
- Damren Room, Rotary Room, The Arcade (Lebanon)

## Deployment

### Production Environment
- **Host**: Ubuntu Server on library infrastructure
- **Deployment**: Docker Compose with versioned images
- **Networking**: Bound to localhost:5000, proxied through nginx
- **Automation**: systemd timer fetches data every 15 minutes (24/7)
- **Status**: Production deployment serving 40+ library staff

### Infrastructure as Code

**Dockerfile**
- Multi-stage build with Python 3.14
- Non-root user for security
- uv for dependency management
- Granian WSGI server for production

**Docker Compose**
- Development: nginx + Flask with live reload
- Production: Minimal Flask-only configuration
- Named volumes for data persistence
- Timezone-aware logging

**Makefile**
Common developer workflows:
```bash
make dev-up           # Start local development
make dev-rebuild      # Rebuild after code changes
make release VERSION=v1.0  # Build and push to registry
make release-clean    # Force rebuild after dependency updates
```

## Technical Highlights

### HTMX Patterns
```html
<!-- Dynamic room switching -->
<a hx-get="/api/bookings?id=106060" 
   hx-target="#bookings" 
   hx-swap="innerHTML">Community Room</a>

<!-- Out-of-band timestamp update -->
<div id="timestamp" hx-swap-oob="true">
  Last updated: {{ timestamp }}
</div>
```

### Flask Route Design
```python
@app.get("/api/bookings")
def bookings():
    space_id = get_space_id_from_request()  # Request context proxy
    data = get_booking_data()
    booking_days = group_bookings_by_day(data, space_id)
    return render_template("bookings.html", 
                         bookings=booking_days, 
                         space=SPACES.get(space_id))
```

### nginx Routing
```nginx
location /api/bookings {
    proxy_pass http://localhost:5000/;  # Strips prefix
    # Flask routes: /refresh, /fetch, / (not /api/bookings/*)
}
```

## Repository Structure
```
libcal-bookings/
├── app.py                    # Flask application and routes
├── fetcher.py                # LibCal API integration
├── bookings.py               # Booking data model
├── templates/
│   ├── bookings.html         # HTMX booking cards
│   └── error.html            # Error state handling
├── Dockerfile                # Multi-stage production build
├── compose.yml               # Production deployment
├── compose.dev.yml           # Development environment
├── Makefile                  # Developer workflow automation
├── systemd/
│   ├── libcal-bookings-fetch.service
│   └── libcal-bookings-fetch.timer
└── docs/
    ├── architecture.md       # System design documentation
    └── screenshots/
```

## Development Workflow

**Local Development**
```bash
# Start dev environment (nginx + Flask)
make dev-up

# Make code changes
# ...

# Rebuild and restart
make dev-rebuild

# View logs
make dev-logs
```

**Production Release**
```bash
# Update dependencies if needed
uv lock --upgrade
uv sync

# Build and push with version tag
make release-clean VERSION=v1.1

# Deploy to server
ssh server
cd /opt/libcal-bookings
docker compose pull
docker compose up -d
```

## Lessons Learned

### Technical Growth
- **Request Context**: Leveraged Flask's request proxy pattern for cleaner function design without explicit parameter passing
- **HTMX Patterns**: Implemented out-of-band swaps for updating multiple page sections from single responses
- **Docker Layer Caching**: Learned to use `--no-cache` builds after dependency updates to ensure security patches applied
- **Separation of Concerns**: Decoupled Flask routes from nginx URL structure for better portability

### Product Decisions
- **MVP Focus**: Deferred health check endpoints and edge-case UX fixes until actual user feedback indicated need
- **Real User Testing**: Iterated on UI based on feedback from custodian and deputy director before deployment
- **Operational Simplicity**: Chose 24/7 automated refresh over complex time-windowing (96 API calls/day well within limits)

## Future Enhancements

### Month 6: CI/CD Pipeline (Planned)
- GitHub Actions for automated testing and image builds
- Automated deployment to staging environment
- Container vulnerability scanning with Trivy
- Automated rollback on deployment failures

### Potential Features
- Email/SMS alerts for after-hours bookings
- Historical booking analytics
- Room availability predictions
- Calendar export functionality

## Technologies Demonstrated

**Backend Development**
- Python Flask with production WSGI (Granian)
- OAuth 2.0 API authentication
- Environment-based configuration
- Structured logging

**Frontend Development**
- HTMX for progressive enhancement
- Alpine.js for reactive UI components
- Responsive CSS with mobile-first design
- Semantic HTML and accessibility

**DevOps & Infrastructure**
- Docker containerization with security best practices
- Docker Compose for multi-environment deployments
- nginx reverse proxy configuration
- systemd for process automation
- Makefile for developer workflows

**Production Operations**
- Versioned Docker images in registry
- Blue-green deployment capability
- Container security scanning
- Zero-downtime deployments

## Live Deployment

This application is currently running in production at Lebanon Public Libraries, serving approximately 40 staff members across two library locations.

---

**Project Timeline**: Week 9 of 6-month DevOps learning roadmap  
**Initial Release**: January 2026  
**Current Version**: v1.0.1