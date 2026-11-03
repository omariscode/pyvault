from typing import Any

class Vault:

    def __init__(self):
        self._storage = {}

    def set(self, key: str | int, value: Any) -> dict | str :
        """Function for set data into a our storage"""
        if key in self._storage:
            raise KeyError(f"This key already exists: {key}")
        self._storage[key] = value
        return self._storage

    def get(self, key: str | int) -> str:
        """Function to get data using a specific key from our storage"""
        return self._storage.get(key, "Key not found")

    def exists(self, key: str | int) -> bool:
        """Verify if a key exists"""
        if key in self._storage:
            return True
        return False

    def delete(self, key: str | int):
        """Delete a specific key-value from storage"""
        if key not in self._storage:
            raise KeyError(f"This key does not exist in storage: {key}")

        self._storage.pop(key)
        return "Key-Value deleted from storage"

    def clear(self) -> str:
        """Clear all storage"""
        self._storage.clear()
        return "Storage cleaned"

    def __len__(self):
        """Return the length of the storage"""
        return len(self._storage)
