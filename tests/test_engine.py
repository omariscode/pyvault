import pytest

from pyvault.engine import Vault

class TestVault:

    def setup_method(self):
        self.vault = Vault()

    def test_set(self):
        self.vault.set("1", {"nome": "omar"})

        assert self.vault._storage["1"] == {"nome": "omar"}

    def test_set_chave_ja_existe(self):
        self.vault.set(1, {"nome": "omar"})

        with pytest.raises(KeyError) as exc_info:
            self.vault.set(1, {"nome": "asiel"})  # segunda vez → deve falhar

        assert "This key already exists" in str(exc_info.value)
        assert "1" in str(exc_info.value)

    def test_get(self):
        self.vault.set("1", {"nome": "omar"})

        assert self.vault.get("1") == {"nome": "omar"}

    def test_get_not_found(self):
        self.vault.set("1", {"nome": "omar"})

        assert self.vault.get("2") == "Key not found"

    def test_exists(self, key="1"):
        self.vault.set("1", {"nome": "omar"})

        assert self.vault.exists("1") is True
        assert self.vault.exists("2") is False

    def test_clear(self):
        self.vault.set("1", {"nome": "omar"})

        assert self.vault.clear() == "Storage cleaned"

    def test_len(self):
        self.vault.set("1", {"nome": "omar"})
        self.vault.set("2", {"nome": "omar"})
        self.vault.set("3", {"nome": "omar"})
        self.vault.set("4", {"nome": "omar"})

        assert self.vault.__len__() == 4
