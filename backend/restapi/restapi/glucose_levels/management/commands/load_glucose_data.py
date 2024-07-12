import pandas as pd
import os
from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Load glucose data from a CSV file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("file_path", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        for user_file in os.listdir(file_path):
            if user_file.endswith(".csv"):
                with open(os.path.join(file_path, user_file), "r") as f:
                    df = pd.read_csv(f)
                    print(df.head())
                    print(user_file)
