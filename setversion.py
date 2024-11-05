import subprocess
import tomllib
import sys
import pathlib
import argparse


def run_bash_command(command: str):
    process = subprocess.Popen(["bash", "-c", command], stdout=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print(
            f"{command} failed: Return code = {process.returncode}, Process Output = {str(out)}, Error Output = {str(err)}",
            file=sys.stderr,
        )
        sys.exit(2)


def main(*, package: str, tag: bool = True):
    # Collects version from the pyproject.toml file
    try:
        with open(file="pyproject.toml", mode="rb") as f:
            print("pyproject.toml file accessed")
            pyproject_dict = tomllib.load(f)
    except IOError:
        print("pyproject.toml not found", file=sys.stderr)
        sys.exit(1)

    version = pyproject_dict["tool"]["poetry"]["version"]

    # If tag is true, then performs the git commit and tag
    if tag:
        commit_and_tag_str = f'git add -A && git commit -m "{version}" && git tag -a {version} -m "{version}"'
        run_bash_command(commit_and_tag_str)

    package_root_dir = pathlib.Path(__file__).parent / package
    print(package_root_dir)
    if not package_root_dir.is_dir():
        print(f"{package} not found", file=sys.stderr)
        sys.exit(1)

    with open(package_root_dir / "_version.py", "w") as f:
        print("#-# generated by setversion.py #-#", file=f)
        print(f'VERSION="{version}" # pragma: no cover', file=f)


if __name__ == "__main__":
    description = """Automatically replaces the internal version with the one in the current pyproject.toml. 
        Optionally will also automatically create a git commit and git tag after versioning.
        """

    parser = argparse.ArgumentParser(prog="setversion", description=description)
    parser.add_argument(
        "package", type=str, help="The package name in this directory to be versioned"
    )
    parser.add_argument(
        "--tag", action="store_true", help="Git commit and tag after setting version"
    )
    parser.add_argument(
        "--push", action="store_true", help="Pushes the tag to remote origin"
    )

    args = parser.parse_args()
    main(package=args.package, tag=args.tag)
