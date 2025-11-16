class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None

        self.author = author      # use setter
        self.magazine = magazine  # use setter
        self._set_title(title)    # private initializer to bypass immutability

        Article.all.append(self)

    # PRIVATE method: used only inside __init__ to set title ONCE.
    def _set_title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Title should not change after initialization (immutable)
        # Ignore all future attempts to change it.
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value


class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # name is immutable → ignore changes
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({mag.category for mag in mags})


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None

        self.name = name
        self.category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [article.title for article in arts]

    def contributing_authors(self):
        counts = {}
        for article in self.articles():
            author = article.author
            counts[author] = counts.get(author, 0) + 1

        authors = [a for a, c in counts.items() if c > 2]
        return authors if authors else None
