import requests

ZENODO_API_URL = "https://zenodo.org/api/records"
ORCID = "0009-0000-8858-4992"

def fetch_zenodo_publications(orcid):
    query = f"creators.orcid:{orcid}"
    response = requests.get(f"{ZENODO_API_URL}?q={query}&size=100")
    response.raise_for_status()
    results = response.json()["hits"]["hits"]
    return results

def write_markdown(publications):
    with open("zenodo-publications.md", "w", encoding="utf-8") as f:
        f.write("# Zenodo Publications\n\n")
        if not publications:
            f.write("No publications found.\n")
            return
        for pub in publications:
            title = pub['metadata'].get('title', 'No Title')
            url = pub['links'].get('html', '')
            creators = ', '.join([
                c.get('name', '') for c in pub['metadata'].get('creators', [])
            ])
            f.write(f"- [{title}]({url}) — {creators}\n")

if __name__ == "__main__":
    publications = fetch_zenodo_publications(ORCID)
    write_markdown(publications)
