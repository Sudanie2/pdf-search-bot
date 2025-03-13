from google.cloud import storage

BUCKET_NAME = "your-bucket-name"
PDF_PATH = "documents/sample.pdf"

def download_pdf():
    """GCSからPDFをダウンロード"""
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(PDF_PATH)
    
    blob.download_to_filename("../data/temp.pdf")
    print(f"{PDF_PATH} をダウンロードしました")
    return "../data/temp.pdf"
