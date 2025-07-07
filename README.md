# B2 Uploader

A minimal Python utility to upload files to Backblaze B2 Cloud Storage using `b2sdk`.

## 🚀 Installation

```bash
pip install git+https://github.com/yourusername/backblaze-b2-uploader.git
```

## 📤 Usage

```python
from b2_uploader.uploader import upload_file

upload_file(
    local_path='path/to/file.jpg',
    bucket_name='your-bucket',
    dest_path='uploads/file.jpg',
    key_id='your_key_id',
    app_key='your_app_key'
)
```

## 🧪 Testing

```bash
pytest tests
```

## 🛡 License

MIT