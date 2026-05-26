def generate_architecture_diagram(
    architecture
):

    diagram = "User\n↓\n"

    pages = (
        architecture["pages"]
    )

    # Smart ordering
    ordered_pages = []

    if (
        "login_page"
        in pages
    ):
        ordered_pages.append(
            "login_page"
        )

    if (
        "dashboard_page"
        in pages
    ):
        ordered_pages.append(
            "dashboard_page"
        )

    if (
        "payment_page"
        in pages
    ):
        ordered_pages.append(
            "payment_page"
        )

    if (
        "analytics_page"
        in pages
    ):
        ordered_pages.append(
            "analytics_page"
        )

    # add remaining pages
    for page in pages:

        if (
            page
            not in ordered_pages
        ):
            ordered_pages.append(
                page
            )

    # Build diagram
    for page in ordered_pages:

        clean_name = (
            page
            .replace(
                "_",
                " "
            )
            .replace(
                "page",
                ""
            )
            .title()
            .strip()
        )

        diagram += (
            f"{clean_name}\n↓\n"
        )

    diagram += "Database"

    file_path = (
        "generated_project/"
        "architecture_diagram.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            diagram
        )

    return {

        "status":
        "diagram_generated",

        "file":
        file_path,

        "diagram":
        diagram
    }