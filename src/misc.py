class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass


class BabaJan(InformalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        return super().load_data_source(path, file_name)
    def extract_text(self, full_file_name: str) -> dict:
        return super().extract_text(full_file_name)