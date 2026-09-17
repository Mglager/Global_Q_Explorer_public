"""Download a testing-portfolio vintage from global-q.org into data/.

    python scripts/fetch_data.py --vintage 2025
    python scripts/fetch_data.py --vintage 2026 --keep-old

global-q.org republishes the whole library once a year and stamps the last
sample year into every filename, so a new release is a new --vintage. The script
downloads the six size-interacted category archives, the one-way frictions
archive (which is where the size-decile market portfolio lives), and the q5
factor returns, then lays them out the way the app expects:

    data/me_mom_monthly_<v>/portf_me_<code>_monthly_<v>.csv
    data/me_vvg_monthly_<v>/...
    data/me_inv_monthly_<v>/...
    data/me_prof_monthly_<v>/...
    data/me_intan_monthly_<v>/...
    data/me_fric_monthly_<v>/...
    data/portf_me_monthly_<v>.csv
    data/q5_factors_monthly_<v>.csv

Afterwards the metric catalog still has to be checked against the new file list,
because a release can add or drop anomalies. See docs/UPDATING.md.
"""

import argparse
import io
import json
import os
import re
import shutil
import sys
import urllib.request
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")

BASE = "https://global-q.org/uploads/1/2/2/6/122679606"

# archive stem -> destination directory stem
CATEGORY_ARCHIVES = {
    "me_mom": "me_mom",
    "me_vvg": "me_vvg",
    "me_inv": "me_inv",
    "me_prof": "me_prof",
    "me_intan": "me_intan",
    "me_fric": "me_fric",
}

# The published zips have occasionally carried a mis-typed inner folder name
# (the 2025 me_vvg archive unpacks to "me_monthlyl_2025"), so the destination is
# decided by which archive a file came from, never by the folder inside it.


def fetch(url):
    print("  GET {}".format(url))
    request = urllib.request.Request(url, headers={"User-Agent": "Global-Q-Explorer/1.0"})
    with urllib.request.urlopen(request, timeout=180) as response:
        if response.status != 200:
            raise RuntimeError("HTTP {} for {}".format(response.status, url))
        return response.read()


def unpack_csvs(blob, destination):
    """Extract every .csv in the archive flat into destination."""
    os.makedirs(destination, exist_ok=True)
    written = 0
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        for name in archive.namelist():
            if not name.lower().endswith(".csv"):
                continue
            target = os.path.join(destination, os.path.basename(name))
            with archive.open(name) as source, open(target, "wb") as sink:
                shutil.copyfileobj(source, sink)
            written += 1
    return written


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--vintage", required=True,
                        help="last sample year of the release, e.g. 2025")
    parser.add_argument("--keep-old", action="store_true",
                        help="leave any existing vintage in place instead of removing it")
    parser.add_argument("--data-dir", default=DATA, help="target directory (default: data/)")
    args = parser.parse_args()

    if not re.fullmatch(r"\d{4}", args.vintage):
        sys.exit("--vintage must be a four-digit year")

    vintage = args.vintage
    data_dir = args.data_dir
    os.makedirs(data_dir, exist_ok=True)

    if not args.keep_old:
        for entry in sorted(os.listdir(data_dir)):
            path = os.path.join(data_dir, entry)
            is_old_dir = os.path.isdir(path) and re.search(r"_monthly_\d{4}$", entry) \
                and not entry.endswith(vintage)
            is_old_csv = entry.endswith(".csv") and re.search(r"_(\d{4})\.csv$", entry) \
                and not entry.endswith("{}.csv".format(vintage))
            if is_old_dir:
                print("removing old vintage directory {}".format(entry))
                shutil.rmtree(path)
            elif is_old_csv:
                print("removing old vintage file {}".format(entry))
                os.remove(path)

    total = 0
    print("\nCategory archives")
    for stem, dest_stem in CATEGORY_ARCHIVES.items():
        blob = fetch("{}/{}_monthly_{}.zip".format(BASE, stem, vintage))
        destination = os.path.join(data_dir, "{}_monthly_{}".format(dest_stem, vintage))
        if os.path.isdir(destination):
            shutil.rmtree(destination)
        count = unpack_csvs(blob, destination)
        print("    -> {} files in {}".format(count, os.path.basename(destination)))
        total += count

    print("\nMarket portfolio (size deciles, from the one-way frictions archive)")
    blob = fetch("{}/fric_monthly_{}.zip".format(BASE, vintage))
    market_name = "portf_me_monthly_{}.csv".format(vintage)
    found = False
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        for name in archive.namelist():
            if os.path.basename(name) == market_name:
                with archive.open(name) as source, \
                        open(os.path.join(data_dir, market_name), "wb") as sink:
                    shutil.copyfileobj(source, sink)
                found = True
                break
    if not found:
        sys.exit("{} was not in fric_monthly_{}.zip - check the release layout"
                 .format(market_name, vintage))
    print("    -> {}".format(market_name))

    print("\nq5 factor returns")
    factors_name = "q5_factors_monthly_{}.csv".format(vintage)
    blob = fetch("{}/{}".format(BASE, factors_name))
    with open(os.path.join(data_dir, factors_name), "wb") as fh:
        fh.write(blob)
    print("    -> {}".format(factors_name))

    print("\n{} anomaly files, plus the market portfolio and the factor returns."
          .format(total))

    # ---- tell the user whether the catalog still matches the data ----
    catalog_path = os.path.join(REPO, "data", "metrics_catalog.json")
    if os.path.exists(catalog_path):
        with open(catalog_path, encoding="utf-8") as fh:
            catalog = json.load(fh)
        documented = {m["code"] for m in catalog.get("metrics", [])}
        on_disk = {"me"}
        for entry in os.listdir(data_dir):
            full = os.path.join(data_dir, entry)
            if not os.path.isdir(full):
                continue
            for fname in os.listdir(full):
                if fname.endswith(".csv"):
                    stem = os.path.splitext(fname)[0].split("portf_me_")[-1]
                    on_disk.add(re.sub(r"_monthly_\d{4}$", "", stem))

        new_codes = sorted(on_disk - documented)
        gone_codes = sorted(documented - on_disk)
        print("\nCatalog check")
        if not new_codes and not gone_codes:
            print("    catalog matches the data - nothing to do.")
        else:
            if new_codes:
                print("    NEW anomalies with no catalog entry: {}".format(new_codes))
            if gone_codes:
                print("    catalog entries no longer in the data: {}".format(gone_codes))
            print("    -> update data/metrics_catalog.json, then run "
                  "scripts/build_docs.py (see docs/UPDATING.md).")
    else:
        print("\nNo metrics_catalog.json found - see docs/UPDATING.md.")


if __name__ == "__main__":
    main()
