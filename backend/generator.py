def extract_intent(prompt):

    prompt_lower = (
        prompt.lower()
        .strip()
    )

    features = []

    # Smart keyword mapping
    feature_map = {

        # Login
        "login": "login",
        "auth": "login",
        "authentication": "login",
        "signin": "login",
        "signup": "login",

        # Dashboard
        "dashboard": "dashboard",

        # Payments
        "payment": "payments",
        "payments": "payments",
        "subscription": "payments",
        "subscriptions": "payments",
        "billing": "payments",

        # Analytics
        "analytics": "analytics",
        "reports": "analytics",

        # Contacts
        "contacts": "contacts",
        "crm": "contacts",

        # Chat
        "chat": "chat",
        "messaging": "chat",

        # Profile
        "profile": "profile",

        # Admin
        "admin": "admin_panel",
        "admin panel": "admin_panel"
    }

    # Detect features
    for keyword in feature_map:

        if keyword in prompt_lower:

            feature = feature_map[
                keyword
            ]

            if (
                feature
                not in features
            ):
                features.append(
                    feature
                )

    roles = ["user"]

    if (
        "admin_panel"
        in features
    ):
        roles.append(
            "admin"
        )

    return {
        "app_type":
        "web_application",

        "features":
        features,

        "roles":
        roles
    }


def system_design(intent):

    pages = []

    feature_to_page = {

        "login":
        "login_page",

        "dashboard":
        "dashboard_page",

        "payments":
        "payment_page",

        "analytics":
        "analytics_page",

        "contacts":
        "contacts_page",

        "chat":
        "chat_page",

        "profile":
        "profile_page",

        "admin_panel":
        "admin_page"
    }

    for feature in (
        intent["features"]
    ):

        if (
            feature
            in feature_to_page
        ):

            page = (
                feature_to_page[
                    feature
                ]
            )

            if page not in pages:
                pages.append(
                    page
                )

    entities = [
        "users"
    ]

    if (
        "payments"
        in intent["features"]
    ):
        entities.append(
            "subscriptions"
        )

    if (
        "contacts"
        in intent["features"]
    ):
        entities.append(
            "contacts"
        )

    flows = []

    if (
        "login"
        in intent["features"]
    ):
        flows.append(
            "authentication"
        )

    if (
        "payments"
        in intent["features"]
    ):
        flows.append(
            "payment_processing"
        )

    if (
        "chat"
        in intent["features"]
    ):
        flows.append(
            "real_time_chat"
        )

    return {
        "pages":
        pages,

        "entities":
        entities,

        "flows":
        flows
    }


def generate_schema(
    intent,
    architecture
):

    ui_schema = {
        "pages":
        architecture["pages"],

        "components":
        []
    }

    for page in (
        architecture["pages"]
    ):

        elements = [
            "header",
            "sidebar",
            "content"
        ]

        # Smart UI components
        if page == "login_page":
            elements.extend([
                "email_input",
                "password_input",
                "login_button"
            ])

        elif page == "payment_page":
            elements.extend([
                "pricing_cards",
                "payment_button"
            ])

        elif page == "dashboard_page":
            elements.extend([
                "stats_card",
                "charts"
            ])

        ui_schema[
            "components"
        ].append({

            "page":
            page,

            "elements":
            elements
        })

    api_schema = []

    for entity in (
        architecture["entities"]
    ):

        api_schema.append({
            "endpoint":
            f"/api/{entity}",

            "method":
            "GET"
        })

    db_schema = []

    for entity in (
        architecture["entities"]
    ):

        fields = [
            "id",
            "created_at"
        ]

        if entity == "users":
            fields.extend([
                "email",
                "password"
            ])

        if entity == "subscriptions":
            fields.extend([
                "plan_name",
                "price",
                "status"
            ])

        db_schema.append({
            "table_name":
            entity,

            "fields":
            fields
        })

    auth_rules = {
        "roles":
        intent["roles"],

        "permissions":
        {}
    }

    for role in (
        intent["roles"]
    ):

        if role == "admin":

            auth_rules[
                "permissions"
            ][role] = [

                "read",
                "write",
                "delete"
            ]

        else:

            auth_rules[
                "permissions"
            ][role] = [
                "read"
            ]

    return {

        "ui_schema":
        ui_schema,

        "api_schema":
        api_schema,

        "db_schema":
        db_schema,

        "auth_rules":
        auth_rules
    }