import sqlite3
from tools.db_helpers import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("PRAGMA journal_mode=WAL;")
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS claim_contradictions (

    contradiction_id TEXT PRIMARY KEY,

    claim_id_a TEXT NOT NULL,
    claim_id_b TEXT NOT NULL,

    contradiction_strength REAL CHECK(
        contradiction_strength >= 0
        AND contradiction_strength <= 1
    ),

    noted_by TEXT NOT NULL,

    noted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(claim_id_a)
        REFERENCES claims(claim_id)
        ON DELETE CASCADE,

    FOREIGN KEY(claim_id_b)
        REFERENCES claims(claim_id)
        ON DELETE CASCADE

)
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_contradiction_claim_a
ON claim_contradictions(claim_id_a);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_contradiction_claim_b
ON claim_contradictions(claim_id_b);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_contradiction_strength
ON claim_contradictions(contradiction_strength);
""")

conn.commit()
print("Claim contradictions table created successfully!")
conn.close()