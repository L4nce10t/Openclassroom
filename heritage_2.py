"""Définit les classes propres à notre forum. ;)"""


class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        print(f"Fichier '{self.name}'.")


class ImageFile():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display(self):
        print(f"On affiche {self.name}")


class JPG(ImageFile):

    def __init__(self, name, type):
        super().__init__(name, type)

    def display(self):
        super().display()
        print(f"L'image {self.name} est de type {self.type}")


class GIF(ImageFile):

    def __init__(self, name, type):
        super().__init__(name, type)

    def display(self):
        super().display()
        print(f"L'image {self.name} est un gif")


class User:
    """Utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom d'utilisateur et le mot de passe."""
        self.username = username
        self.password = password

    def login(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        """Créé un nouveau fil de discussion."""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        """représentation de l'utilisateur."""
        return self.username


class Moderator(User):
    """Utilisateur modérateur."""

    def edit(self, post, content):
        """Modifie un message."""
        post.content = content

    def delete(self, thread, post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]


class Post:
    """Message."""

    def __init__(self, user, time_posted, content):
        """Initialise l'utilisateur, la date et le contenu."""
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        """Affiche le message."""
        print(f"Message posté par {self.user} le {self.time_posted}:")
        print(self.content)


class FilePost(Post):
    """Message comportant un fichier."""

    def __init__(self, user, time_posted, content, file):
        """Initialise le fichier."""
        self.user = user
        self.time_posted = time_posted
        self.content = content
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display()
        print("pièce jointe:")
        self.file.display()


class Thread:
    """Fil de discussions."""

    def __init__(self, title, time_posted, post):
        """Initialise le titre, la date et les posts.

        Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourrons s'ajouter qu'ultérieurement.
        En effet, on ne créé pas directement un nouveau fil avec des réponses. ;)
        """
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.posts.append(post)


jesuisuneimage = JPG('chat', 'jpg')
jesuisuneimage.display()
