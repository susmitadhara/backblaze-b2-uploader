import unittest
from unittest.mock import patch, MagicMock
from b2_uploader import uploader

class TestUploader(unittest.TestCase):
    @patch('b2_uploader.uploader.B2Api')
    def test_upload_file(self, mock_b2_api):
        mock_bucket = MagicMock()
        mock_uploaded = MagicMock(
            file_name='test.txt',
            file_id='123abc',
            bucket_name='my-bucket',
            upload_timestamp=1234567890
        )
        mock_bucket.upload_bytes.return_value = mock_uploaded
        mock_b2_api.return_value.get_bucket_by_name.return_value = mock_bucket

        with patch('builtins.open', unittest.mock.mock_open(read_data=b"data")):
            result = uploader.upload_file(
                'test.txt', 'my-bucket', 'dest/test.txt', 'key-id', 'app-key'
            )

        self.assertEqual(result['file_name'], 'test.txt')
        self.assertEqual(result['file_id'], '123abc')
        self.assertIn('public_url', result)

    def test_get_public_url(self):
        url = uploader.get_public_url("my-bucket", "images/photo.jpg")
        self.assertEqual(
            url,
            "https://f000.backblazeb2.com/file/my-bucket/images/photo.jpg"
        )

    @patch('b2_uploader.uploader.B2Api')
    def test_get_private_file_url(self, mock_b2_api):
        mock_bucket = MagicMock()
        mock_bucket.get_download_url_by_name.return_value = "https://example.com/private"
        mock_b2_api.return_value.get_bucket_by_name.return_value = mock_bucket

        url = uploader.get_private_file_url("my-bucket", "file.txt", "key-id", "app-key")
        self.assertEqual(url, "https://example.com/private")

    @patch('b2_uploader.uploader.B2Api')
    def test_get_signed_url(self, mock_b2_api):
        mock_bucket = MagicMock()
        mock_bucket.get_download_url_by_name.return_value = "https://example.com/signed"
        mock_auth = MagicMock()
        mock_auth.authorization_token = "securetoken123"
        mock_bucket.get_download_authorization.return_value = mock_auth
        mock_b2_api.return_value.get_bucket_by_name.return_value = mock_bucket

        signed_url = uploader.get_signed_url("my-bucket", "file.txt", "key-id", "app-key")
        self.assertIn("Authorization=securetoken123", signed_url)
        self.assertTrue(signed_url.startswith("https://example.com/signed"))

if __name__ == '__main__':
    unittest.main()