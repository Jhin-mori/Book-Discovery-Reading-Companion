import requests


class OpenLibraryClient:

    SEARCH_URL = "https://openlibrary.org/search.json"

    def search_by_title(self, title):

        params = {
    "title": title,
    "fields": "title,author_name,isbn,first_publish_year,subject,number_of_pages_median,cover_i"
}

        response = requests.get(
            self.SEARCH_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("docs", [])
    
