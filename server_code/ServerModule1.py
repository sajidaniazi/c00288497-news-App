from datetime import datetime
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
@anvil.server.callable
def add_article(article_dict):
  app_tables.articles.add_row(
    created=datetime.now(),
    **article_dict
  )
