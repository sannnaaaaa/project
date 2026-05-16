import os


def allowed_file(filename):

    allowed_extensions = {"png", "jpg", "jpeg"}

    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in allowed_extensions


def create_folder(folder_path):

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def save_result(file_path, soil_type, crops):

    with open(file_path, "w") as file:

        file.write(f"Detected Soil Type: {soil_type}\n\n")

        file.write("Recommended Crops:\n")

        for crop in crops:
            file.write(f"- {crop}\n")