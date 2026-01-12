import uuid

class DataFactory:
    @staticmethod
    def get_random_string(length=5):
        return uuid.uuid4().hex[:length]

    @staticmethod
    def get_unique_name(prefix="Test"):
        return f"{prefix}_{DataFactory.get_random_string()}"

    @staticmethod
    def get_unique_id(prefix="ID"):
        return f"{prefix}{DataFactory.get_random_string()}"
