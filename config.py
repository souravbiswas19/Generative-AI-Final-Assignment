"""Configuration file"""
import os
chroma_instances = {}
def fetch_google_key():
    """Fetch Google API key from Environment variable"""
    return os.environ.get('GOOGLE_API_KEY')
#calling the GOOGLE_API_KEY from user environment variable
#End of File