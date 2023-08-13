import pathway as pw
import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

data_dir = os.environ.get("DATA_DIR", "./data/")


class DataSourceType(Enum):
    CSV = "CSV"


def connect(source_type, schema, params=None):
    if source_type == DataSourceType.CSV:
        return read_from_csv(data_dir, schema)
    else:
        raise ValueError(f"Unsupported data source type: {source_type}")


def read_from_csv(data_dir, schema):
    sales_data = pw.io.csv.read(
        data_dir,
        schema=schema,
        mode="streaming",
        autocommit_duration_ms=50,
    )
    return sales_data