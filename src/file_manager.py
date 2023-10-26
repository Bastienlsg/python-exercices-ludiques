import os


class FileManager:
    """
    A utility class for file management operations.
    """

    @staticmethod
    def get_valid_file_choice(file_list):
        """
        Prompt the user to choose a file from a list of files and return the chosen number.

        Args:
            file_list (list): List of available file names.

        Returns:
            int: The number of the file chosen by the user.

        Raises:
            ValueError: In case of incorrect user input.
        """
        while True:
            try:
                choice = int(input("Veuillez entrer le numéro du fichier que vous souhaitez utiliser : "))
                if 1 <= choice <= len(file_list):
                    return choice
                else:
                    print("Numéro de fichier invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")

    @staticmethod
    def display_available_json_files(directory_path):
        """
        Display the list of available JSON files in a given directory.

        Args:
            directory_path (str): The path of the directory containing the files.

        Returns:
            list: List of available file names.

        If no JSON files are found, this function will print a message and return None.
        """
        file_list = [file_name for file_name in os.listdir(directory_path) if file_name.endswith(".json")]

        if not file_list:
            print("Aucun fichier JSON disponible dans le répertoire.")
            return None

        print("\nFichiers JSON disponibles dans le répertoire :")
        for i, file_name in enumerate(file_list, start=1):
            print(f"{i}. {file_name}")

        return file_list
