import psycopg2
from config import DB_PARAMS   # dictionary with connection parameters

def connect():
    # establishes a connection to the PostgreSQL database
    return psycopg2.connect(**DB_PARAMS)

def save_result(username, score, level):
    # saves the result of the game to the game_sessions table
    conn = connect(); cur = conn.cursor()
    # adding a player if it is not already available
    cur.execute("INSERT INTO players(username) VALUES(%s) ON CONFLICT(username) DO NOTHING", (username,))
    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    pid = cur.fetchone()[0]

    # recording the result of the game
    cur.execute("INSERT INTO game_sessions(player_id, score, level_reached, played_at) VALUES(%s,%s,%s, CURRENT_TIMESTAMP)", 
                (pid, score, level))
    conn.commit(); conn.close()

def top10():
    # returns the top 10 best results
    conn = connect(); cur = conn.cursor()
    cur.execute("""SELECT p.username, g.score, g.level_reached, g.played_at
                   FROM game_sessions g JOIN players p ON g.player_id=p.id
                   ORDER BY g.score DESC LIMIT 10""")
    rows = cur.fetchall(); conn.close()
    return rows

def personal_best(username):
    # returns the best score of a specific player
    conn = connect(); cur = conn.cursor()
    cur.execute("""SELECT MAX(score) FROM game_sessions g
                   JOIN players p ON g.player_id=p.id WHERE p.username=%s""", (username,))
    best = cur.fetchone()[0]; conn.close()
    return best or 0