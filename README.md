# B2 Uploader

A minimal Python utility to upload and access files on Backblaze B2 Cloud Storage using `b2sdk`.

## 🚀 Installation

```bash
pip install git+https://github.com/susmitadhara/backblaze-b2-uploader.git
```

Or clone and install locally:

```bash
git clone https://github.com/susmitadhara/backblaze-b2-uploader.git
cd backblaze-b2-uploader
pip install -e .
```

## 📤 Usage

```python
from b2_uploader.uploader import upload_file

upload_file(
    local_path='path/to/photo.jpg',
    bucket_name='your-bucket',
    dest_path='uploads/photo.jpg',
    key_id='your_key_id',
    app_key='your_app_key'
)

print(result['public_url'])
```

The `upload_file()` function returns:
```json
{
  "file_name": "photo.jpg",
  "file_id": "4_z...",
  "bucket_name": "your-bucket",
  "upload_timestamp": 1722302123,
  "public_url": "https://f000.backblazeb2.com/file/your-bucket/uploads/photo.jpg"
}
```

---

## 🔐 Accessing Files

### 🌍 Public URL
If your bucket is public:
```python
from b2_uploader.uploader import get_public_url
url = get_public_url('your-bucket', 'uploads/photo.jpg')
```

### 🔒 Private URL
```python
from b2_uploader.uploader import get_private_file_url
url = get_private_file_url('your-bucket', 'uploads/photo.jpg', key_id, app_key)
```

### ⏳ Signed URL (Temporary Access)
```python
from b2_uploader.uploader import get_signed_url
url = get_signed_url(
    bucket_name='your-bucket',
    file_path='uploads/photo.jpg',
    key_id='your_key_id',
    app_key='your_app_key',
    valid_seconds=600
)
```

---

## 📦 Package Structure
```
b2_uploader/
├── uploader.py

setup.py
README.md
tests/
├── test_uploader.py
```

---

## 🧪 Testing

```bash
pytest tests
```

---

## 🛡 License

MIT