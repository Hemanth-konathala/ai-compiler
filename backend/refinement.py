def refine_system(
    intent,
    architecture,
    schemas
):

    changes = []

    # Payments require login
    if (
        "payments"
        in intent["features"]
        and "login"
        not in intent["features"]
    ):

        intent[
            "features"
        ].append(
            "login"
        )

        changes.append(
            "Login added automatically for payments"
        )

    # Rebuild architecture
    from generator import (
        system_design,
        generate_schema
    )

    architecture = (
        system_design(
            intent
        )
    )

    schemas = (
        generate_schema(
            intent,
            architecture
        )
    )

    return {

        "status":
        "refinement_completed",

        "changes":
        changes,

        "intent":
        intent,

        "architecture":
        architecture,

        "schemas":
        schemas
    }