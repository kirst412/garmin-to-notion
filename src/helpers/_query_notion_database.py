from functools import lru_cache
from typing import Any

from notion_client import Client


@lru_cache(maxsize=128)
def _get_data_source_id(client: Client, database_id: str) -> str:
    database = client.databases.retrieve(database_id)
    data_sources = database.get("data_sources", [])

    if len(data_sources) != 1:
        raise ValueError(
            f"Expected exactly one data source for Notion database {database_id}, "
            f"found {len(data_sources)}."
        )

    return data_sources[0]["id"]


def query_database(client: Client, database_id: str, **kwargs: Any) -> Any:
    data_source_id = _get_data_source_id(client, database_id)
    return client.data_sources.query(data_source_id, **kwargs)
