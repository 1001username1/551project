import sqlite3

class PlayerManager:
    def __init__(self, db_name="players.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                name TEXT PRIMARY KEY,
                wins INTEGER DEFAULT 0,
                losses INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_player(self, name):
        try:
            self.cursor.execute("INSERT INTO players (name, wins, losses) VALUES (?, 0, 0)", (name,))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def update_score(self, name, result):
        if result == "win":
            self.cursor.execute("UPDATE players SET wins = wins + 1 WHERE name = ?", (name,))
        elif result == "loss":
            self.cursor.execute("UPDATE players SET losses = losses + 1 WHERE name = ?", (name,))
        self.conn.commit()  # Commit changes


    def get_all_players(self):
        self.cursor.execute("SELECT name, wins, losses FROM players")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
