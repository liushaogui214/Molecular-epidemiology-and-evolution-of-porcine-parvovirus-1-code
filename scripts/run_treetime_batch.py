import argparse
import logging
import subprocess
import sys
from pathlib import Path


def find_single_file(input_dir: Path, suffix: str) -> Path:
    matches = sorted(input_dir.glob(f"*{suffix}"))
    if not matches:
        raise FileNotFoundError(f"No {suffix} file found in {input_dir}")
    if len(matches) > 1:
        logging.warning("Multiple %s files found; using %s", suffix, matches[0])
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run TreeTime for the PPV1 VP2 sequence alignment."
    )
    parser.add_argument(
        "--input-dir",
        default=Path("data/treetime"),
        type=Path,
        help="Directory containing one FASTA alignment, one Newick tree, and one CSV date file.",
    )
    parser.add_argument(
        "--outdir",
        default=Path("results/treetime"),
        type=Path,
        help="Directory for TreeTime output files.",
    )
    args = parser.parse_args()

    logging.basicConfig(
        filename="treetime_log.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    input_dir = args.input_dir
    output_dir = args.outdir
    output_dir.mkdir(parents=True, exist_ok=True)

    fasta_file = find_single_file(input_dir, ".fasta")
    tree_file = find_single_file(input_dir, ".nwk")
    metadata_file = find_single_file(input_dir, ".csv")

    command = [
        sys.executable,
        "-m",
        "treetime",
        "--aln",
        str(fasta_file),
        "--tree",
        str(tree_file),
        "--dates",
        str(metadata_file),
        "--outdir",
        str(output_dir),
    ]

    logging.info("Running command: %s", " ".join(command))
    subprocess.run(command, check=True)
    logging.info("TreeTime analysis completed successfully.")


if __name__ == "__main__":
    main()
