import os
import h5py
import json
from os.path import join
from datetime import datetime
from typing import List
from .entities import Loger, Metric, Error
from .llm import analyze_error_with_openai
class DataRepository:
    def __init__(self, data_directory: str):
        self.data_directory = data_directory

    def _encode_data(self, data: dict) -> bytes:
        """Encode dictionary data to bytes."""
        return json.dumps(data).encode('utf-8')

    def _decode_data(self, data: bytes) -> dict:
        """Decode bytes data to dictionary."""
        return json.loads(data.decode('utf-8'))

    def _ensure_directory_exists(self, directory: str):
        """Ensure that the directory exists, create it if it doesn't."""
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _get_partitioned_file_path(self, partition: str, data_type: str) -> str:
        """Generate the file path for the partitioned data."""
        return join(self.data_directory, f"{data_type}s_{partition}.h5")

    def _get_current_partition(self) -> str:
        """Generate the current partition based on the current date."""
        return datetime.now().strftime("%Y-%m-%d")

    def save_log(self, log: Loger):
        partition = self._get_current_partition()
        log_file_path = self._get_partitioned_file_path(partition, "log")
        self._ensure_directory_exists(self.data_directory)
        with h5py.File(log_file_path, "a") as file:
            if "logs" not in file:
                file.create_dataset("logs", data=self._encode_data([]))
            logs = self._decode_data(file["logs"][()])
            logs.append(log.dict())
            file["logs"][()] = self._encode_data(logs)

    def save_metric(self, metric: Metric):
        partition = self._get_current_partition()
        metric_file_path = self._get_partitioned_file_path(partition, "metric")
        self._ensure_directory_exists(self.data_directory)
        with h5py.File(metric_file_path, "a") as file:
            if "metrics" not in file:
                file.create_dataset("metrics", data=self._encode_data([]))
            metrics = self._decode_data(file["metrics"][()])
            metrics.append(metric.dict())
            file["metrics"][()] = self._encode_data(metrics)

    def save_error(self, error: Error):
        if (error.message["type"] == "error.exception"):
            aianalysis = analyze_error_with_openai(error.message["message"])
            error.message["ai_analysis"] = aianalysis
        partition = self._get_current_partition()
        error_file_path = self._get_partitioned_file_path(partition, "error")
        self._ensure_directory_exists(self.data_directory)
        with h5py.File(error_file_path, "a") as file:
            if "errors" not in file:
                file.create_dataset("errors", data=self._encode_data([]))
            errors = self._decode_data(file["errors"][()])
            errors.append(error.dict())
            file["errors"][()] = self._encode_data(errors)
                
    def retrieve_data(self, data_type: str, application: str, start_date: str = None, end_date: str = None, page: int = 1, limit: int = 1000) -> List[dict]:
        partition = self._get_current_partition()
        partition_directory = join(self.data_directory)
        print(partition_directory)
        if not os.path.exists(partition_directory):
            return {"error": f"Partition directory for '{application}' does not exist.", "code": 500}
        
        # Filter files based on data type and optional date range
        filtered_files = []
        for file_name in os.listdir(partition_directory):
            if file_name.startswith(f"{data_type}s_") and file_name.endswith(".h5"):
                if start_date and end_date:
                    file_date = file_name.split("_")[1].split(".")[0]
                    if start_date <= file_date <= end_date:
                        filtered_files.append(join(partition_directory, file_name))
                else:
                    filtered_files.append(join(partition_directory, file_name))

        if not filtered_files:
            return {"error": f"No {data_type} files found in the specified date range.", "code": 404}

        all_data = []
        for data_file_path in filtered_files:
            try:
                with h5py.File(data_file_path, "r") as file:
                    for dataset_name in file:
                        dataset = file[dataset_name][()]
                        decoded_data = json.loads(dataset.decode('utf-8'))
                        all_data.append(decoded_data)
            except FileNotFoundError:
                return {"error": f"File '{data_file_path}' not found."}

        # Implement pagination and limit
        start_index = (page - 1) * limit
        end_index = start_index + limit
        paginated_data = all_data[start_index:end_index]

        return paginated_data

