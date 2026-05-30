import sqlite3
from tools.db_helpers import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("PRAGMA journal_mode=WAL;")
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS research_sessions (

    session_id TEXT PRIMARY KEY,

    original_claim TEXT NOT NULL,

    normalized_claim TEXT,

    claim_type TEXT CHECK(
        claim_type IN (
            'factual',
            'causal',
            'predictive',
            'comparative',
            'ethical',
            'vague'
        )
    ),

    classification_confidence REAL CHECK(
        classification_confidence >= 0
        AND classification_confidence <= 1
    ),

    complexity_score REAL CHECK(
        complexity_score >= 0
        AND complexity_score <= 1
    ),

    assumptions_made TEXT,

    current_stage TEXT DEFAULT 'intake' CHECK(
        current_stage IN (
            'intake',
            'agent1_complete',
            'agent2_complete',
            'agent3_complete',
            'agent4_complete',
            'agent5_complete',
            'agent6_complete',
            'completed',
            'failed'
        )
    ),

    final_verdict TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_session_current_stage
ON research_sessions(current_stage);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_session_claim_type
ON research_sessions(claim_type);
""")

conn.commit()
print("Research sessions table created successfully!")
conn.close()