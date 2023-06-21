'''
Sparsity-based Hypergraph Dualization

This module contains a few utility functions to use the binary file shd contained in the scripts folder.

For further information see: http://research.nii.ac.jp/~uno/code/shd.html
'''
import os
import pathlib
import subprocess

from typing import List

# this variable is the maximum limit time to run the script shd
TIMEOUT=5

def shd_path() -> str:
  pca_shd_exec_path = "scripts/shd"
  if os.name != 'nt':
      # @TODO hack to add current shd library path in non-windows operative system
      current_path = str(pathlib.Path(__file__).parent.resolve())
      pca_shd_exec_path = current_path + "/scripts/shd"
  return pca_shd_exec_path    

def fromEdgesFileToHypergraph(edges_file_path: str):
    """
    Given a file path which target a file containing the edges of a hypergraph with the format one-edge per line.
    Returns the result of generating a hypergraph in the shd format.
    Example:
    Hypergraph file
    0,3
    0,5
    1,3
    1,4
    2,3
    2,4
    2,5
    Hypergraph result
    3 5 4
    3 5 1 2
    0 3 4 2
    0 1 2
    4
    0
    0
    0
    2
    2
    """
    args = [shd_path(), "0", edges_file_path, "-"]
    return run(args)

def run(args: List[str]) -> str | None:
    try:
        """
        @TODO: it is better to use run instead of Popen + communicate in this case.
        see: https://docs.python.org/3/library/subprocess.html#subprocess.run
        """
        result = subprocess.run(args, timeout=TIMEOUT, check=True, text=True, capture_output=True)
        return result.stdout if result.stdout else None
    except FileNotFoundError as exc:
        print(f"Process failed because the executable could not be found.\n{exc}")
    except subprocess.CalledProcessError as exc:
        print(
            f"Process failed because did not return a successful return code. "
            f"Returned {exc.returncode}\n{exc}"
        )
    except subprocess.TimeoutExpired as exc:
        print(f"Process timed out.\n{exc}")
    return None
