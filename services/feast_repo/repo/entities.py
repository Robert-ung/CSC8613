from feast import Entity

# Définition de l'entité principale "user"
user = Entity(
    name="user",                        # nom logique de l’entité
    join_keys=["user_id"],              # clé utilisée pour relier les features
    description="Représente un client StreamFlow identifié par son user_id",
)
