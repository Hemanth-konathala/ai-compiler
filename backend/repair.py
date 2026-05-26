def repair_system(
    intent,
    architecture,
    schemas,
    validation
):

    repaired_items = []

    errors = (
        validation[
            "errors"
        ]
    )

    # Fix missing users API
    if (
        "Login page requires users API"
        in errors
    ):

        schemas[
            "api_schema"
        ].append({

            "endpoint":
            "/api/users",

            "method":
            "GET"
        })

        repaired_items.append(
            "Users API added"
        )

    # Fix missing users table
    if (
        "Login page requires users table"
        in errors
    ):

        schemas[
            "db_schema"
        ].append({

            "table_name":
            "users",

            "fields":
            [
                "id",
                "email",
                "password"
            ]
        })

        repaired_items.append(
            "Users table added"
        )

    # Fix subscriptions API
    if (
        "Payment page requires subscriptions API"
        in errors
    ):

        schemas[
            "api_schema"
        ].append({

            "endpoint":
            "/api/subscriptions",

            "method":
            "GET"
        })

        repaired_items.append(
            "Subscriptions API added"
        )

    # Fix subscriptions table
    if (
        "Payment page requires subscriptions table"
        in errors
    ):

        schemas[
            "db_schema"
        ].append({

            "table_name":
            "subscriptions",

            "fields":
            [
                "id",
                "plan_name",
                "price"
            ]
        })

        repaired_items.append(
            "Subscriptions table added"
        )

    status = (
        "no_repair_needed"
    )

    if (
        len(repaired_items)
        > 0
    ):

        status = (
            "repair_completed"
        )

    return {

        "status":
        status,

        "repaired_items":
        repaired_items
    }