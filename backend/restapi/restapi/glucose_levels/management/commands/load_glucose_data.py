from datetime import datetime
import pandas as pd
import os
from django.core.management.base import BaseCommand, CommandParser

from restapi.glucose_levels.models import User, GlucoseLevel


# poetry run python manage.py load_glucose_data ./restapi/glucose_levels/data_files/
class Command(BaseCommand):
    help = "Load glucose data from a CSV file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("file_path", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        for user_file in os.listdir(file_path):
            if user_file.endswith(".csv"):
                with open(os.path.join(file_path, user_file), "r") as f:
                    df = pd.read_csv(f, skiprows=1)
                    user_id = user_file.split(".")[0]
                    user, _ = User.objects.get_or_create(user_id=user_id)
                for _, row in df.iterrows():
                    GlucoseLevel.objects.create(
                        user=user,
                        device=row["Gerät"],
                        serial_number=row["Seriennummer"],
                        device_timestamp=datetime.strptime(
                            row["Gerätezeitstempel"], "%d-%m-%Y %H:%M"
                        ),
                        record_type=int(row["Aufzeichnungstyp"]),
                        glucose_value_history=(
                            float(row["Glukosewert-Verlauf mg/dL"])
                            if row["Glukosewert-Verlauf mg/dL"]
                            else None
                        ),
                    )
        self.stdout.write(self.style.SUCCESS("Successfully loaded glucose data"))
