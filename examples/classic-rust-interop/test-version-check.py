#!/usr/bin/env python3
"""Exercise build-rust.sh's version gate without a Rust installation or SDK."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


class VersionCheckTest(unittest.TestCase):
    def run_gate(self, version_output, rustc_exit=0):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "rust").mkdir()
            (root / "bin").mkdir()
            shutil.copyfile(Path(__file__).with_name("build-rust.sh"), root / "build-rust.sh")
            (root / "version.txt").write_text(version_output)
            rustc = root / "bin/rustc"
            rustc.write_text(
                '#!/bin/sh\nset -e\ncat "$VERSION_FILE"\n'
                f'exit {rustc_exit}\n'
            )
            cargo = root / "bin/cargo"
            cargo.write_text('#!/bin/sh\nprintf reached > "$CARGO_MARKER"\nexit 73\n')
            rustc.chmod(0o755)
            cargo.chmod(0o755)
            env = dict(os.environ, PATH=str(root / "bin") + os.pathsep + os.environ["PATH"],
                       VERSION_FILE=str(root / "version.txt"), CARGO_MARKER=str(root / "cargo-called"))
            result = subprocess.run(["bash", str(root / "build-rust.sh")], env=env,
                                    capture_output=True, timeout=15)
            return result.returncode, (root / "cargo-called").exists()

    def test_matching_version_reaches_cargo(self):
        self.assertEqual(self.run_gate(self.matching_output()), (73, True))

    def test_matching_version_drains_output_larger_than_pipe_buffer(self):
        self.assertEqual(self.run_gate(self.matching_output() + "extra metadata\n" * 300000), (73, True))

    def test_wrong_version_does_not_reach_cargo(self):
        self.assertEqual(self.run_gate("commit-hash: wrong\n"), (1, False))

    def test_empty_output_does_not_reach_cargo(self):
        self.assertEqual(self.run_gate(""), (1, False))

    def test_rustc_failure_after_matching_output_is_preserved(self):
        self.assertEqual(self.run_gate(self.matching_output(), rustc_exit=42), (42, False))

    @staticmethod
    def matching_output():
        return "commit-hash: 2036fdd24f77d607dcfaa24c48fbe85d3f785823\n"


if __name__ == "__main__":
    unittest.main()
