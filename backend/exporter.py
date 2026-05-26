import json


def export_blueprint(data):

    filename = "generated_blueprint.json"

    with open(
        filename,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return {
        "status":
        "export_success",

        "file":
        filename
    }