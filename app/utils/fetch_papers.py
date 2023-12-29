import json
import urllib.request
import xml.etree.ElementTree as ET
from typing import List


def fetch_papers() -> List[str]:
    """Fetches papers from the arXiv API returns them as a list of strings."""

    url = (
        "http://export.arxiv.org/api/query?search_query=ti:llama&start=0&max_results=70"
    )

    response = urllib.request.urlopen(url)

    data = response.read().decode("utf-8")

    root = ET.fromstring(data)

    papers_list = []

    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text

        summary = entry.find("{http://www.w3.org/2005/Atom}summary").text

        paper_info = f"Title: {title}\nSummary: {summary}\n"

        papers_list.append(paper_info)

    return papers_list


def load_papers_from_json(filename="papers.json"):
    """Loads papers from a json file and returns them as a list of strings."""

    with open(filename, "r") as f:
        papers_list = json.load(f)

    return papers_list


def save_papers_to_json(papers_list: List[str], filename="papers.json"):
    """Saves a list of papers to a file."""

    with open(filename, "w") as f:
        for paper in papers_list:
            json.dump(paper, f)
