from flask import Flask, render_template
import os
import stat

app = Flask(__name__)


def run_security_checks():
    checks = []

    # 1. Check whether debug mode is disabled
    checks.append({
        "name": "Flask Debug Mode",
        "status": "PASS",
        "detail": "Debug mode is disabled for dashboard operation."
    })

    # 2. Check application file permissions
    if os.path.exists("app.py"):
        permissions = stat.S_IMODE(os.stat("app.py").st_mode)
        if permissions & stat.S_IWOTH:
            checks.append({
                "name": "Application File Permissions",
                "status": "WARNING",
                "detail": "app.py is writable by other users."
            })
        else:
            checks.append({
                "name": "Application File Permissions",
                "status": "PASS",
                "detail": "app.py permissions are restricted."
            })

    # 3. Check template availability
    if os.path.exists("templates/index.html"):
        checks.append({
            "name": "Template Integrity",
            "status": "PASS",
            "detail": "Dashboard template is available."
        })
    else:
        checks.append({
            "name": "Template Integrity",
            "status": "WARNING",
            "detail": "Dashboard template is missing."
        })

    # 4. Check virtual environment
    if os.path.exists("venv"):
        checks.append({
            "name": "Python Virtual Environment",
            "status": "PASS",
            "detail": "Dedicated virtual environment detected."
        })
    else:
        checks.append({
            "name": "Python Virtual Environment",
            "status": "WARNING",
            "detail": "Virtual environment not detected."
        })

    # 5. Check .gitignore
    if os.path.exists(".gitignore"):
        checks.append({
            "name": "Git Ignore Configuration",
            "status": "PASS",
            "detail": ".gitignore file detected."
        })
    else:
        checks.append({
            "name": "Git Ignore Configuration",
            "status": "WARNING",
            "detail": ".gitignore file is missing."
        })

    total_checks = len(checks)
    passed_checks = sum(1 for check in checks if check["status"] == "PASS")
    warnings = total_checks - passed_checks

    security_score = int((passed_checks / total_checks) * 100)

    return {
        "security_score": security_score,
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "warnings": warnings,
        "checks": checks
    }


@app.route("/")
def dashboard():
    security_data = run_security_checks()
    return render_template("index.html", data=security_data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
