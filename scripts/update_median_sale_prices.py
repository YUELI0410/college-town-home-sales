"""Refresh the college-town median sale price table in index.html."""

import csv
from collections import defaultdict
from html import escape
from math import floor
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "college_town_home_sales.csv"
PAGE_PATH = ROOT / "index.html"
MINIMUM_PRICE = 10_000


def main():
    prices_by_location = defaultdict(list)
    with CSV_PATH.open(encoding="utf-8", newline="") as source:
        for sale in csv.DictReader(source):
            price = int(sale["sale_price"])
            if price >= MINIMUM_PRICE:
                location = (sale["city"], sale["state"])
                prices_by_location[location].append(price)

    summaries = [
        (median(prices), city, state, len(prices))
        for (city, state), prices in prices_by_location.items()
    ]
    summaries.sort(key=lambda summary: (-summary[0], summary[1], summary[2]))

    rows = []
    for median_price, city, state, count in summaries:
        rounded_price = floor(median_price + 0.5)
        rows.append(
            f'        <tr><th scope="row">{escape(city)}</th>'
            f"<td>{escape(state)}</td><td>{count:,}</td>"
            f"<td>${rounded_price:,}</td></tr>"
        )

    page = PAGE_PATH.read_text(encoding="utf-8")
    before, body = page.split("      <tbody>\n", 1)
    _, after = body.split("      </tbody>", 1)
    updated_page = before + "      <tbody>\n" + "\n".join(rows) + "\n      </tbody>" + after
    if updated_page != page:
        PAGE_PATH.write_text(updated_page, encoding="utf-8")


if __name__ == "__main__":
    main()
