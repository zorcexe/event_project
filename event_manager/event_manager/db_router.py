class ExternalReadOnlyRouter:
    """
    definiert 3 Aktionen:
    - db_for_read: Datenbank zum Lesen wählen
    - db_for_write: Welche Datenbank soll zum schreiben genommen?
    - allow_migrate: verhindert Schemaänderungen
    """

    router_app_labels = {"external_app"}

    def db_for_read(self, model, **hints):
        """Welche DB soll zum Lesen genutzt werden."""
        # Wenn das Model aus external_app ist, wollen wir external zum Lesen nutzen
        if model._meta.app_label in self.router_app_labels:
            return "external"
        return None  # für alle anderen Apps wird default-DB verwendet

    def db_for_write(self, model, **hints):
        """In welche DB soll geschrieben werden?"""
        # Wenn das Model aus external_app ist, wollen wir Schreiben verhindern
        if model._meta.app_label in self.router_app_labels:
            raise RuntimeError("External ist eine Read-only Datenbank")
        return None  # für alle anderen Apps wird default-DB verwendet

    def allow_migrate(self, db, app_label, **hints):
        """Für welche Datenbanken sind Migrationen erlaubt?"""
        if app_label in self.router_app_labels:
            return False  # keine Migration
        return None
