import os
import tempfile
from organizer.core import organizar_archivos

def test_file_organization():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "test.pdf")

        with open(file_path, "w") as f:
            f.write("test")

        config = {
            "documents": ["pdf"]
        }

        organizar_archivos(tmpdir, config)

        expected = os.path.join(tmpdir, "documents", "test.pdf")
        assert os.path.exists(expected)
