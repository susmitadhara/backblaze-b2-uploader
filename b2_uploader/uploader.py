import os
from b2sdk.v2 import InMemoryAccountInfo, B2Api

def get_b2_api(key_id: str, app_key: str) -> B2Api:
    info = InMemoryAccountInfo()
    b2_api = B2Api(info)
    b2_api.authorize_account("production", key_id, app_key)
    return b2_api

def upload_file(local_path: str, bucket_name: str, dest_path: str, key_id: str, app_key: str) -> dict:
    """Uploads a file to Backblaze B2"""
    b2_api = get_b2_api(key_id, app_key)
    bucket = b2_api.get_bucket_by_name(bucket_name)
    with open(local_path, 'rb') as file:
        file_info = {
            'fileName': os.path.basename(local_path)
        }
        uploaded = bucket.upload_bytes(file.read(), dest_path, file_info=file_info)
        return {
            'file_name': uploaded.file_name,
            'file_id': uploaded.file_id,
            'bucket_name': uploaded.bucket_name,
            'upload_timestamp': uploaded.upload_timestamp,
            'public_url': get_public_url(bucket_name, dest_path)
        }
    
def get_public_url(bucket_name: str, file_path: str) -> str:
    """Returns the public URL of a file (if bucket is public)"""
    return f"https://f000.backblazeb2.com/file/{bucket_name}/{file_path}"

def get_private_file_url(bucket_name: str, file_path: str, key_id: str, app_key: str) -> str:
    """Get private download URL (requires bucket to be private)"""
    b2_api = get_b2_api(key_id, app_key)
    bucket = b2_api.get_bucket_by_name(bucket_name)
    return bucket.get_download_url_by_name(file_path)

def get_signed_url(bucket_name: str, file_path: str, key_id: str, app_key: str, valid_seconds: int = 3600) -> str:
    """Generate a signed temporary URL for private files"""
    b2_api = get_b2_api(key_id, app_key)
    bucket = b2_api.get_bucket_by_name(bucket_name)
    auth = bucket.get_download_authorization(
        file_name_prefix=file_path,
        valid_duration_in_seconds=valid_seconds
    )
    download_url = bucket.get_download_url_by_name(file_path)
    return f"{download_url}?Authorization={auth.authorization_token}"