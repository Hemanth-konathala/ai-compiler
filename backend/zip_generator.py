import zipfile
import os


def create_project_zip():

    project_folder = "generated_project"

    zip_filename = "generated_project.zip"

    with zipfile.ZipFile(
        zip_filename,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for root, dirs, files in os.walk(
            project_folder
        ):

            for file in files:

                file_path = os.path.join(
                    root,
                    file
                )

                zipf.write(
                    file_path,
                    os.path.relpath(
                        file_path,
                        project_folder
                    )
                )

    return {
        "status":
        "zip_created",

        "file":
        zip_filename
    }