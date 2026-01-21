import os

from ase.io import read, write


def find_input_path(base_dir: str, idx: int) -> str | None:
    direct = os.path.join(base_dir, f"{idx}.extxyz")
    if os.path.isfile(direct):
        return direct

    fallback = os.path.join(base_dir, str(idx), "allegro_dataset.extxyz")
    if os.path.isfile(fallback):
        return fallback

    return None


def main() -> None:
    base_dir = os.path.dirname(__file__)
    merged = []

    for i in range(1, 12):
        path = find_input_path(base_dir, i)
        if not path:
            print(f"skip missing extxyz for {i}")
            continue
        merged.extend(read(path, index=":"))
        print(f"read: {path}")

    if not merged:
        raise SystemExit("no input extxyz files found")

    output_path = os.path.join(base_dir, "merged.extxyz")
    write(output_path, merged)
    print(f"wrote: {output_path}")


if __name__ == "__main__":
    main()
