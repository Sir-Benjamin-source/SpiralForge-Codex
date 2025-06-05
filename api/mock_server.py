# api/mock_server.py: Mock API server for /enhance endpoint
from enhance_endpoint import enhance
import json

class MockAPIServer:
    def __init__(self):
        self.requests_served = 0

    def handle_request(self, text, config=None):
        """
        Simulate /enhance API call.
        Input: text (str), config (dict, optional)
        Output: JSON string with certification result
        """
        result = enhance(text, config)
        self.requests_served += 1
        # Mock logging to Legal Evidence Vault
        self.log_to_vault(result)
        return json.dumps(result, indent=2)

    def log_to_vault(self, result):
        """
        Mock logging to Legal Evidence Vault.
        Input: result (dict)
        """
        # Future: Save to persistent storage
        pass

if __name__ == "__main__":
    server = MockAPIServer()
    sample_text = "The sky is blue."
    response = server.handle_request(sample_text)
    print(response)
