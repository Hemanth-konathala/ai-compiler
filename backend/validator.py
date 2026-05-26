def validate_system(
    intent,
    architecture,
    schemas
):

    errors = []

    pages = (
        architecture["pages"]
    )

    api_endpoints = []

    db_tables = []

    for api in (
        schemas["api_schema"]
    ):

        api_endpoints.append(
            api["endpoint"]
        )

    for table in (
        schemas["db_schema"]
    ):

        db_tables.append(
            table["table_name"]
        )

    # ----------------
    # Basic validation
    # ----------------

    if len(pages) == 0:

        errors.append(
            "No pages generated"
        )

    if (
        len(
            schemas[
                "db_schema"
            ]
        ) == 0
    ):

        errors.append(
            "No database schema found"
        )

    # ----------------
    # Login consistency
    # ----------------

    if (
        "login_page"
        in pages
    ):

        if (
            "/api/users"
            not in api_endpoints
        ):

            errors.append(
                "Login page requires users API"
            )

        if (
            "users"
            not in db_tables
        ):

            errors.append(
                "Login page requires users table"
            )

    # ----------------
    # Payment consistency
    # ----------------

    if (
        "payment_page"
        in pages
    ):

        if (
            "/api/subscriptions"
            not in api_endpoints
        ):

            errors.append(
                "Payment page requires subscriptions API"
            )

        if (
            "subscriptions"
            not in db_tables
        ):

            errors.append(
                "Payment page requires subscriptions table"
            )

    # ----------------
    # Dashboard consistency
    # ----------------

    if (
        "dashboard_page"
        in pages
    ):

        if (
            "/api/users"
            not in api_endpoints
        ):

            errors.append(
                "Dashboard requires users API"
            )

    # ----------------
    # Analytics consistency
    # ----------------

    if (
        "analytics_page"
        in pages
    ):

        if (
            "/api/users"
            not in api_endpoints
        ):

            errors.append(
                "Analytics requires users API"
            )

    validation_status = (
        "valid"
    )

    if (
        len(errors)
        > 0
    ):

        validation_status = (
            "failed"
        )

    return {

        "status":
        validation_status,

        "errors":
        errors
    }


def handle_failures(
    intent
):

    warnings = []

    clarification_needed = []

    assumptions = []

    features = (
        intent["features"]
    )

    # Smart fallback
    if (
        len(features)
        == 0
    ):

        assumptions.append(
            "Default dashboard app generated"
        )

        features.append(
            "dashboard"
        )

    # Payments require login
    if (
        "payments"
        in features
        and
        "login"
        not in features
    ):

        warnings.append(
            "Payments usually require authentication"
        )

        assumptions.append(
            "Login enabled automatically"
        )

        features.append(
            "login"
        )

    # Clarification
    if (
        len(features)
        <= 1
    ):

        if (
            "login"
            not in features
        ):

            clarification_needed.append(
                "Do you need login?"
            )

        if (
            "dashboard"
            not in features
        ):

            clarification_needed.append(
                "Do you need dashboard?"
            )

        if (
            "payments"
            not in features
        ):

            clarification_needed.append(
                "Do you need payments?"
            )

    status = "clear"

    if (
        len(
            clarification_needed
        )
        > 0
        or
        len(
            warnings
        )
        > 0
    ):

        status = (
            "needs_attention"
        )

    return {

        "status":
        status,

        "warnings":
        warnings,

        "clarification_needed":
        clarification_needed,

        "assumptions":
        assumptions
    }