"""
Single script used during CI/CD build process to download NLTK assets
"""

import nltk

nltk.data.path.append('./nltk_data')
nltk.download('punkt', download_dir='./nltk_data')
