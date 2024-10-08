Password Manager mit Verschlüsselung

Dieser Python-Code implementiert einen einfachen Passwort-Manager mit Verschlüsselung. Er ermöglicht es, Passwörter sicher zu speichern und anzuzeigen. Die Passwörter werden mit der Fernet-Verschlüsselung verschlüsselt, um die Sicherheit der gespeicherten Daten zu gewährleisten.
Voraussetzungen

    Python 3.x
    cryptography-Modul (installierbar mit pip install cryptography)

Funktionen

    Passwörter hinzufügen: Nutzer können Benutzernamen und Passwörter eingeben, die dann verschlüsselt und in einer Datei gespeichert werden.
    Passwörter anzeigen: Zeigt die Benutzernamen und die entschlüsselten Passwörter an.
    Daten persistent speichern: Die verschlüsselten Passwörter werden in einer Textdatei gespeichert, und der Verschlüsselungsschlüssel wird in einer separaten Datei aufbewahrt.

Anleitung

    Schlüssel generieren: Vor der ersten Verwendung muss der Verschlüsselungsschlüssel generiert und gespeichert werden. Dies kann mit der auskommentierten write_key()-Funktion erfolgen:

    python

    def write_key():
        key = Fernet.generate_key()
        with open("path/to/mykey.key", "wb") as f:
            f.write(key)

    Programm verwenden:
        Hinzufügen: Wähle die Option "a", um einen neuen Benutzernamen und ein Passwort hinzuzufügen.
        Anzeigen: Wähle die Option "v", um die gespeicherten Passwörter anzuzeigen.
        Beenden: Wähle "q", um das Programm zu beenden.

    Dateistruktur:
        mykey.key: Enthält den Fernet-Verschlüsselungsschlüssel.
        password3.txt: Speichert die verschlüsselten Passwörter.

Sicherheitshinweis

Bewahren Sie den Schlüssel und die Passwortdatei an einem sicheren Ort auf. Wenn der Schlüssel verloren geht, können die Passwörter nicht wiederhergestellt werden.