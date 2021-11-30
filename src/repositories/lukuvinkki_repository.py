from entities.lukuvinkki import Lukuvinkki  # pylint: disable=unused-import


class LukuvinkkiRepository:
    def __init__(self):
        self._lukuvinkkis = []

    def find_all(self):
        return self._lukuvinkkis

    def create(self, lukuvinkki):
        self._lukuvinkkis.append(lukuvinkki)

    def check_lukuvinkki(self, title, author):
        for lukuvinkki in self._lukuvinkkis:
            if title == lukuvinkki.title() and author == lukuvinkki.author():
                return True
        return False

    def delete_all(self):
        del self._lukuvinkkis[:]


lukuvinkki_repository = LukuvinkkiRepository()
