class WhatsAppSender:
    def __init__(self, api_key=None):
        self.api_key = api_key
        
    def is_configured(self):
        return False  # Simple placeholder for now
        
    def send_report_link(self, report_path):
        # Placeholder - will implement WhatsApp integration later
        print("📱 WhatsApp integration placeholder")
        return None
