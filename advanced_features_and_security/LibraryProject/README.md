# Permissions and Groups Setup

## Custom Permissions
Defined in `Article` model:
- can_view: Allows viewing of articles
- can_create: Allows creation of new articles
- can_edit: Allows editing of existing articles
- can_delete: Allows deletion of articles

## Groups
- **Viewers** → can_view
- **Editors** → can_create, can_edit
- **Admins** → all permissions

Run `python manage.py init_groups` to create groups and assign permissions automatically.

## Enforcement
Each view uses Django’s `@permission_required` decorator to restrict access.


# Security Review: HTTPS Enforcement

## Summary
This document outlines the HTTPS and security header configurations applied to the Django project.

### Key Settings in `settings.py`
- `SECURE_SSL_REDIRECT = True`: Forces all HTTP requests to use HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enables HTTP Strict Transport Security for one year.
- `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True`: Cookies sent only over HTTPS.
- `X_FRAME_OPTIONS = "DENY"`: Prevents clickjacking attacks.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Blocks MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Activates browser XSS protection.

### Deployment Configuration
- SSL/TLS certificates are configured using Let's Encrypt.
- Nginx is configured to proxy HTTPS traffic to the Django app.
- All HTTP requests are redirected to HTTPS.

### Testing Performed
1. Verified HTTPS redirection from HTTP URLs.
2. Checked that cookies include the `Secure` attribute.
3. Tested HSTS headers with browser developer tools.
4. Validated CSP, X-Frame-Options, and other headers via browser security report.

### Future Improvements
- Add Content Security Policy (CSP) headers to further restrict content sources.
- Regularly renew SSL certificates.
- Run automated vulnerability scans using tools like OWASP ZAP.
