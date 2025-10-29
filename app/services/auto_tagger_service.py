import app.constants as constants

class AutoTaggerService:
  def get_tag(self, text: str) -> list[str]:
    tags = set()
    words = text.lower().split()

    for tag in constants.STATIC_TAGS:
      if tag.lower() in words:
        tags.add(tag)

    return list(tags)