import os
from urllib.parse import urlparse
from typing import Optional

expansionPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '.\scripts\expansion'))

def load_file_from_url(
        url: str,
        *,
        model_dir: str,
        progress: bool = True,
        file_name: Optional[str] = None,
) -> str:
    """Download a file from `url` into `model_dir`, using the file present if possible.

    Returns the path to the downloaded file.
    """
    os.makedirs(model_dir, exist_ok=True)
    if not file_name:
        parts = urlparse(url)
        file_name = os.path.basename(parts.path)
    cached_file = os.path.abspath(os.path.join(model_dir, file_name))
    if not os.path.exists(cached_file):
        print(f'Downloading: "{url}" to {cached_file}\n')
        from torch.hub import download_url_to_file
        download_url_to_file(url, cached_file, progress=progress)
    return cached_file


def download_models():
    load_file_from_url(
        url='https://huggingface.co/lllyasviel/misc/resolve/main/fooocus_expansion.bin',
        model_dir=expansionPath,
        file_name='pytorch_model.bin'
    )

    return

download_models()