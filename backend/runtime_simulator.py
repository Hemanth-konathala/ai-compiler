def simulate_runtime(
    architecture,
    schemas
):

    checks = []

    execution_status = True

    # Check pages
    if len(
        architecture["pages"]
    ) > 0:

        checks.append(
            "Pages loaded successfully"
        )

    else:
        execution_status = False
        checks.append(
            "Page loading failed"
        )

    # Check APIs
    if len(
        schemas["api_schema"]
    ) > 0:

        checks.append(
            "API routes generated"
        )

    else:
        execution_status = False
        checks.append(
            "API generation failed"
        )

    # Check database
    if len(
        schemas["db_schema"]
    ) > 0:

        checks.append(
            "Database schema valid"
        )

    else:
        execution_status = False
        checks.append(
            "Database schema missing"
        )

    # Final status
    if execution_status:
        status = "SUCCESS"
    else:
        status = "FAILED"

    return {
        "execution_status":
        status,

        "runtime_checks":
        checks
    }