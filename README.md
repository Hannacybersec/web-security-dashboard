cat > README.md <<'EOF'
# Web Security Dashboard

A Python Flask-based defensive security dashboard that performs local security checks and displays the results through a web interface.

## Features

- Local security monitoring dashboard
- Automated security checks
- Security score calculation
- Application file permission check
- Template integrity check
- Python virtual environment check
- Git ignore configuration check
- PASS/WARNING status display
- Responsive web interface

## Security Checks

The dashboard currently checks:

1. Flask debug mode configuration
2. Application file permissions
3. Dashboard template availability
4. Python virtual environment availability
5. `.gitignore` configuration

The security score is calculated based on the percentage of passed checks.

## Technologies

- Python 3
- Flask
- HTML5
- CSS3
- Kali Linux
- Git & GitHub

## Testing

The dashboard was tested locally using Flask.

Test result:

- Security Score: 100/100
- Total Checks: 5
- Passed Checks: 5
- Warnings: 0

## Run Locally

Activate the virtual environment:

```bash
source venv/bin/activate
